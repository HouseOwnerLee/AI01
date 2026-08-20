import torch
import torch.nn.functional as F
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from konlpy.tag import Okt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import random

okt = Okt()


def convert_to_noun_form(word):
    """
    '모르다' -> '모름', '신나다' -> '신남', '먹다' -> '먹음' 등
    동사/형용사 원형을 자연스러운 명사형으로 변환합니다.
    """
    if not word.endswith('다') or len(word) <= 1:
        return word  # '비', '기분' 같은 명사는 그대로 통과

    stem = word[:-1]  # '다'를 뗀 앞부분 (예: '모르', '먹')
    last_char = stem[-1]  # 마지막 글자 (예: '르', '먹')

    # 한글 유니코드 계산을 통해 받침 유무 확인
    char_code = ord(last_char) - 0xAC00
    if char_code < 0 or char_code > 11171:
        return word

    jongseong = char_code % 28  # 종성(받침) 위치 확인

    # 1. 받침이 없는 경우 (예: 모르 -> 모름, 신나 -> 신남)
    if jongseong == 0:
        new_char = chr(ord(last_char) + 16)  # 'ㅁ' 받침 추가
        return stem[:-1] + new_char

    # 2. 받침이 'ㄹ'인 경우 (예: 살다 -> 삶, 만들다 -> 만듦)
    elif jongseong == 8:
        new_char = chr(ord(last_char) + 2)  # 'ㄻ' 받침으로 변경
        return stem[:-1] + new_char

    # 3. 그 외 받침이 이미 있는 경우 (예: 먹다 -> 먹음, 잡다 -> 잡음)
    else:
        return stem + "음"


def convert_to_search_keyword(word):
    clean_word = word.strip(".,!?\"'")

    # 1. 의미 없는 부사 및 감탄사 블랙리스트 방어
    blacklist_words = ["도대체", "진짜", "정말", "너무", "완전", "그냥", "막상", "어차피", "갑자기"]
    if clean_word in blacklist_words:
        return ""

    # stem=True로 기본 원형 복원 진행
    pos_tags = okt.pos(clean_word, stem=True)
    if not pos_tags:
        return clean_word

    # 2. 사용할 핵심 품사(명사, 동사, 형용사)만 허용하는 화이트리스트 방식 적용
    valid_morphemes = [
        (text, pos) for text, pos in pos_tags
        if pos in ['Noun', 'Verb', 'Adjective']
    ]

    if not valid_morphemes:
        return ""

    # 가장 핵심이 되는 첫 번째 형태소의 단어와 품사 추출
    base_word, pos = valid_morphemes[0]

    # 3. 한 글자짜리 동사/형용사나 의미 없는 단어 추가 필터링
    # 예: '해서' -> '하다'(Verb)인데 '하다' 자체는 검색어로 무의미하므로 제외
    if pos in ['Verb', 'Adjective'] and (len(base_word) <= 1 or base_word == '하다'):
        return ""

    return base_word


def recommend_music_by_integrated_pipeline(diary_text, client_secret, model_path="./results/checkpoint-12651"):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    tokenizer = AutoTokenizer.from_pretrained("beomi/KcELECTRA-base")
    model = AutoModelForSequenceClassification.from_pretrained(model_path)
    model.eval()
    model.to(device)

    # 감정 라벨 순서 추출
    if hasattr(model.config, "id2label") and "LABEL" not in str(model.config.id2label):
        emotion_list = [model.config.id2label[i] for i in range(len(model.config.id2label))]
    else:
        emotion_list = ["기쁨", "분노", "불안", "슬픔"]  # 기본 fallback 순서

    # 🔍 1단계: 감정 분석 및 디버깅 로그 출력
    print("원 문장:", diary_text)
    print("🧠 1. 일기 감정 분석 중...")
    inputs_orig = tokenizer(diary_text, return_tensors="pt", truncation=True, max_length=128)

    with torch.no_grad():
        outputs_orig = model(
            input_ids=inputs_orig["input_ids"].to(device),
            attention_mask=inputs_orig["attention_mask"].to(device)
        )
        probs_orig = F.softmax(outputs_orig.logits, dim=-1).squeeze().cpu().numpy()

    final_target_idx = probs_orig.argmax()
    detected_emotion = emotion_list[final_target_idx]
    orig_target_score = probs_orig[final_target_idx]

    # 🚨 [핵심 디버그 프린트] 이 세 줄의 출력을 확인해야 합니다!
    print(f"   ⚠️ [디버그] 현재 인식된 감정 순서 리스트: {emotion_list}")
    print(f"   ⚠️ [디버그] 모델의 생짜 확률 배열: {probs_orig}")
    print(f"   ⚠️ [디버그] 선택된 가장 높은 인덱스(argmax): {final_target_idx}")
    print(f"   ▶ 최종 매칭 결과: [{detected_emotion}] (확률: {orig_target_score * 100:.2f}%)")

    # 🔍 2단계: 키워드 추적 (조사/어미 분리 오류 완벽 해결 버전)
    print("\n🔎 2. 감정 유발 핵심 키워드 추적 중 (형태소 단위 정밀 분석)...")
    stopwords = [
        "오늘", "군은", "오늘은", "오늘도", "어제", "내일", "모레", "요즘", "요즘은", "최근", "그때",
        "지금", "이제", "현재", "아까", "방금", "벌써", "맨날", "항상", "자주", "가끔",
        "평소", "매일", "하루", "갑자기", "드디어", "결국", "마침내", "올해", "이번", "지난",
        "동안", "순간", "아침", "점심", "저녁", "새벽", "주말", "하루종일", "조원", "팀원", "조원들이랑",
        "그리고", "하지만", "그러나", "그래서", "그래도", "그런데", "그렇지만", "그러면",
        "그러니까", "아무튼", "어쨌든", "일단", "역시", "참", "또", "더", "다시", "그냥",
        "너무", "너무나", "진짜", "진짜로", "정말", "정말로", "매우", "아주", "무척", "엄청",
        "상당히", "조금", "약간", "되게", "꽤", "제일", "가장", "훨씬", "많이", "완전", "완전히",
        "나", "나는", "내가", "나를", "우리", "우리는", "우리끼리", "너", "너는",
        "생각", "생각이", "생각을", "소리", "얘기", "이야기", "때문", "때문에", "덕분에",
        "도대체", "막상", "어차피", "만큼", "정도", "경우", "때문", "때문에", "덕분에", "무엇", "무슨", "가지", "번은",
        "모르다", "그렇다", "아니다", "없다", "있다", "같다", "되다", "하다", "보이다", "내리다", '내림',
        "결과", "시험", "과제", "마일스톤", "이유", "사실", "상황", "문제", "내용",
        "행동", "부분", "모습", "소식", "시간", "약속", "시작", "마지막", "처음", "노력",
        "일어나다", "자다", "먹다", "가다", "오다", "하다", "선택", "일어나", "일어나서"
    ]

    # 문장 전체의 원본 형태소와 원형(Stem) 형태소를 문맥에 맞게 각각 추출합니다.
    morphemes_orig = okt.pos(diary_text, stem=False)
    morphemes_stem = okt.pos(diary_text, stem=True)

    # 중요도 테스트를 진행할 후보 단어(원형) 리스트업
    candidate_stems = []
    for i in range(len(morphemes_stem)):
        text_stem, pos = morphemes_stem[i]
        # 명사, 동사, 형용사만 후보로 선정 (의미 없는 단어 및 조사/어미 원천 차단)
        if pos in ['Noun', 'Verb', 'Adjective']:
            if len(text_stem) > 1 and text_stem not in stopwords and text_stem != "하다":
                if text_stem not in candidate_stems:
                    candidate_stems.append(text_stem)

    chosen_keyword = ""
    if candidate_stems:
        word_importance_scores = []
        for target_stem in candidate_stems:
            # 형태소 단위로 해당 단어를 정밀하게 제외한 modified_text 생성
            modified_tokens = []
            for i in range(len(morphemes_stem)):
                orig_text, _ = morphemes_orig[i]
                stem_text, _ = morphemes_stem[i]

                # 현재 검사 중인 단어의 원형과 일치하면 문장에서 완전히 제외
                if stem_text == target_stem:
                    continue
                modified_tokens.append(orig_text)

            modified_text = " ".join(modified_tokens)
            if not modified_text.strip(): continue

            # 모델 예측값 변화 측정 (Occlusion Test)
            inputs_mod = tokenizer(modified_text, return_tensors="pt", truncation=True, max_length=128)
            with torch.no_grad():
                outputs_mod = model(
                    input_ids=inputs_mod["input_ids"].to(device),
                    attention_mask=inputs_mod["attention_mask"].to(device)
                )
                probs_mod = F.softmax(outputs_mod.logits, dim=-1).squeeze().cpu().numpy()

            mod_target_score = probs_mod[final_target_idx]
            word_importance_scores.append((target_stem, -mod_target_score))

        # ... [기존 2단계 루프 맨 하단 점수 정렬 직후 부분] ...
        if word_importance_scores:
            word_importance_scores.sort(key=lambda x: x[1], reverse=True)

            chosen_keyword = ""  # 기본값

            # ↙️ 중요도 순으로 정렬된 단어들을 하나씩 검사하며 최적의 단어 탐색
            for item in word_importance_scores:
                target_stem = item[0]  # 원형 단어 (예: '모르다', '오다', '짜증')
                converted = convert_to_noun_form(target_stem)  # 명사화 (예: '모름', '옴', '짜증')

                # 🚫 [필터링 규칙 1] 원래 동사/형용사였는데 명사화 후 1글자가 되는 단어 및 일상 동사 원형 패스
                # 💡 target_stem 비교군에 "나오다", "자다"를 확실하게 추가합니다.
                if target_stem in ["오다", "나다", "가다", "자다", "보다", "이다", "일어나다", "일어나", "어떻다", "나오다", "자고"] or len(
                        converted) <= 1:
                    if target_stem not in ["비", "화", "돈"]:
                        continue

                # 🚫 [필터링 규칙 2] 구어체 찌꺼기 및 어색한 변환 명사 패스
                # 💡 converted 비교군에 "자고 나옴", "나옴"을 추가합니다.
                if converted in ["뭐람", "그렇다", "어쩌다", "하다", "일어남", "일어나서", "어떻음", "자고 나옴", "나옴"]:
                    continue

                # ✨ 위 필터링을 다 통과한 가장 자연스러운 단어
                chosen_keyword = converted

                # 특정 필수 예외 처리만 살짝 적용
                if chosen_keyword == "비도":
                    chosen_keyword = "비"
                if chosen_keyword == "화가":
                    chosen_keyword = "화"

                break  # 최적의 단어를 찾았으므로 루프 탈출

    print(f"   ▶ 최종 핵심 단어 선정: '{chosen_keyword}'")

    # 💡 [예외 처리] 감정과 키워드가 겹치는지 체크하는 로직
    # 감정 리스트 예시: ["기쁨", "분노", "불안", "슬픔"]
    # 키워드가 이미 감정명과 비슷하다면 키워드만 사용하거나 감정을 우선시함

    # 중복 의미 매핑 (검색 품질 향상)
    overlap_map = {
        "기쁨": ["기쁨", "즐거움", "신남", "행복"],
        "분노": ["분노", "화", "짜증", "분함"],
        "불안": ["불안", "걱정", "초조"],
        "슬픔": ["슬픔", "우울", "눈물"]
    }

    # 감정이 키워드에 포함되어 있는지 확인
    is_overlapping = False
    for label, variations in overlap_map.items():
        if detected_emotion == label and chosen_keyword in variations:
            is_overlapping = True
            break

    # 🎯 3. 최종 스포티파이 검색 쿼리 결정 (예외 처리 적용)
    if is_overlapping:
        # 중복 시 감정 태그만 사용 (더 넓은 범위의 음악 검색 가능)
        chosen_query = f"#{detected_emotion}"
    elif chosen_keyword == "":
        chosen_query = f"#{detected_emotion}"
    else:
        # 겹치지 않으면 키워드 + 감정 조합
        chosen_query = f"#{chosen_keyword} #{detected_emotion}"

    print(f"🎯 3. 최종 스포티파이 검색 쿼리: '{chosen_query}'")

    # 3단계: 스포티파이 검색
    try:
        # 오프셋 범위를 100으로 넓혀 랜덤성 극대화
        random_offset = random.randint(0, 100)

        # 클라이언트 아이디 값
        client_id = "d479ee2e82c14d7eaea40dbe432663d1"
        auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(auth_manager=auth_manager)

        # limit=1로 설정하여 결과 딱 1개만 가져옴
        search_results = sp.search(q=chosen_query, type="track", limit=1, offset=random_offset)
        tracks = search_results.get("tracks", {}).get("items", [])

        # 결과가 없으면 태그 없이 감정으로만 재검색
        if not tracks:
            search_results = sp.search(q=f"#{detected_emotion}", type="track", limit=1, offset=random_offset)
            tracks = search_results.get("tracks", {}).get("items", [])

        print(f"\n🎵 [오늘의 일기 본문 맞춤 추천 음악]")
        print("-" * 70)

        dashboard_data_list = []
        for track in tracks:
            track_name = track.get("name")
            artists = ", ".join([a["name"] for a in track.get("artists", [])])
            images = track.get("album", {}).get("images", [])
            image_url = images[0].get("url") if images else "https://via.placeholder.com/300"
            preview_url = track.get("preview_url")

            print(f"추천곡: {track_name} - {artists}")
            dashboard_data_list.append({
                "rank": 1,
                "title": track_name,
                "artist": artists,
                "image": image_url,
                "preview": preview_url
            })

        return dashboard_data_list

    except Exception as e:
        print(f"❌ 스포티파이 연동 중 오류 발생: {e}")
        return []


if __name__ == "__main__":
    # 테스트용 입력값
    SECRET = "여러분의_스포티파이_클라이언트_시크릿"
    TEXT = "오늘 친구랑 싸워서 너무 속상해."

    # 함수 호출 테스트
    result = recommend_music_by_integrated_pipeline(TEXT, SECRET)
    print(result)