import requests
import pandas as pd


def get_food_safety_data(api_key):
    base_url = f"http://openapi.foodsafetykorea.go.kr/api/{api_key}/C003/json"
    all_data = []
    start_idx = 1
    end_idx = 1000

    while True:
        url = f"{base_url}/{start_idx}/{end_idx}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"서버 에러 발생: {response.status_code}")
            break

        try:
            data = response.json()
        except Exception as e:
            print("JSON 파싱 에러 발생!")
            print("서버 응답 내용:", response.text)
            break

        if 'RESULT' in data and data['RESULT']['CODE'] != 'INFO-000':
            print(f"API 호출 실패: {data['RESULT']['MESSAGE']}")
            break

        if 'C003' not in data or 'row' not in data['C003']:
            break

        rows = data['C003']['row']
        all_data.extend(rows)
        print(f"{start_idx} ~ {len(all_data)}개 수집 중...")

        start_idx += 1000
        end_idx += 1000

        if start_idx > 45000:
            break

    return pd.DataFrame(all_data)

if __name__ == "__main__":
    api_key = input("api key를 입력하시오 : ")
    df = get_food_safety_data(api_key)
    df[['PRDLST_NM', 'BSSH_NM', 'PRDT_SHAP_CD_NM']].to_csv("health_foods.csv", index=False)