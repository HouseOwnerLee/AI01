import urllib.request
import datetime
import json
import csv
from config import *

# 1. 검색 키워드는 아래 형식처럼 입력받도록 한다.
#    검색키워드 입력 => 앤트로픽
# 2. json형식으로 요청한 결과를 csv형식으로 저장한다.
#    저장할 파일명: 검색키워드_naver.csv
# 3. 출력할 데이터는 100개로 한다.

# 네이버 api에 접속해 응답을 받는 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        # 서버에 요청 보냄
        response = urllib.request.urlopen(req)

        # 응답코드가 200일 경우 성공
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            # 받은 데이터를 반환
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearchResult(sNode, search_text, page_start, display):
    # 검색 베이스 url
    base = "https://openapi.naver.com/v1/search"
    # 검색대상
    node = "/%s.json" %sNode

    # urllib.parse.quote() : 문자나 한글 같은 유니코드 문자열을
    # 퍼센트 인코딩(percent encoding)하여 안전한 URL로 변환하는 함수
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text), page_start, display)

    # 전체 요청 URL 완성
    url = base + node + parameters

    # api호출로 받은 데이터
    retData = getRequestUrl(url)
    print(retData)
    if retData == None:
        return None
    else:
        # json.loads(): JSON 형식의 문자열을 파이썬 객체(딕셔너리나 리스트)로 변환하는 함수
        return json.loads(retData)

# api 결과 중 필요한 항목만 뽑아서 jsonResult에 저장
def getPostData(post, jsonResult):
    # 기사 제목
    title = post['title']
    # 기사 원 링크
    originallink = post['originallink']
    # 기사 네이버 링크
    link = post['link']
    # 기사 요약 정보
    description = post['description']
    # 기사가 제공된 시간
    pubDate = post['pubDate']

    jsonResult.append({'title':title, 'description':description,
                       'originallink':originallink, 'link':link,
                       'pubDate':pubDate})
    return

def main():
    jsonResult = []
    sNode = 'news'
    search_text = input("검색키워드 입력 =>").strip()
    display_count = 100

    # 네이버 api를 통해 뉴스 검색 수행
    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    # 데이터가 정상적으로 수신되었고, 검색 결과가 있다면
    if (jsonSearch is not None) and (jsonSearch['display'] != 0):
        # 받아온 결과를 하나씩 뽑아서 jsonResult에 저장
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)

    # 수집된 데이터를 CSV 파일로 저장
    with open("%s_naver.csv" %search_text, "w", encoding="utf8", newline="") as outfile:
        csvWriter = csv.writer(outfile)

        # 키값들을 헤더로 추출
        header = jsonResult[0].keys()
        csvWriter.writerow(header)

        # 각 데이터의 값들을 기록
        for item in jsonResult:
            csvWriter.writerow(item.values())

    print('%s_naver.csv SAVED' %search_text)

if __name__ == '__main__':
    main()