import urllib.request
import datetime
import json
from config import *
import pymysql
import re

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getNaverSearchResult(sNode, search_text, page_start, display):
    # 검색 베이스 url
    base = "https://openapi.naver.com/v1/search"
    # blog
    node = "/%s.json" %sNode

    # urllib.parse.quote() : 문자나 한글 같은 유니코드 문자열을
    # 퍼센트 인코딩(percent encoding)하여 안전한 URL로 변환하는 함수
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text), page_start, display)

    url = base + node + parameters

    retData = getRequestUrl(url)
    print(retData)
    if retData == None:
        return None
    else:
        # json.loads(): JSON 형식의 문자열을 파이썬 객체(딕셔너리나 리스트)로 변환하는 함수
        return json.loads(retData)

def getPostData(post, jsonResult):
    title = post['title']
    description = post['description']
    bloggerlink = post['bloggerlink']
    link = post['link']
    postdate = post['postdate']
    bloggername = post['bloggername']

    jsonResult.append({'title':title, 'description':description,
                       'bloggerlink':bloggerlink, 'link':link,
                       'postdate':postdate, 'bloggername':bloggername})
    return

def main():
    jsonResult = []
    sNode = 'blog'
    search_text = '앤트로픽'
    display_count = 10

    # 첫 번째 검색 요청 (1번째 데이터부터 display_count만큼)
    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)

    # 결과가 있고, 가져온 데이터(display)가 0이 아닐 때까지 반복
    while (jsonSearch != None) and (jsonSearch['display'] != 0):
        # 현재 가져온 결과(items)를 하나씩 꺼내서 jsonResult 리스트에 추가
        for post in jsonSearch['items']:
            getPostData(post, jsonResult)

        # 다음 요청 시작 위치(nStart) 계산
        # 예: 현재 1번부터 100개를 가져왔다면, 다음은 101번부터 가져와야 함
        nStart = jsonSearch['start'] + jsonSearch['display']
        if nStart > 100:
            break

        # 다음 구간의 데이터를 다시 요청
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open("%s_naver_%s.json" %(search_text, sNode), "w", encoding='utf8') as outfile:
        # json 형식으로 변환
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED' %(search_text, sNode))
    save_db(jsonResult)
    print('DB SAVED')

def connect_db():
    dbconn = pymysql.connect(host="localhost",
                             port=3306,
                             user="root",
                             passwd="123456",
                             db="tabledb",
                             charset="utf8")
    return dbconn

def save_db(jsonResult):
    dbconn = connect_db()
    dbcursor = dbconn.cursor()

    dbcursor.execute("drop table if exists naver_blog;")

    dbcursor.execute("""create table if not exists naver_blog(
        id int auto_increment primary key,
        title varchar(100),
        bloggername varchar(50),
        description varchar(500),
        bloggerlink varchar(200),
        link varchar(200),
        postdate varchar(100));""")

    sql = "insert into naver_blog(title, bloggername, description, bloggerlink,link, postdate) values (%s, %s, %s, %s, %s, %s)"
    for rec in jsonResult:
        try:
            dbcursor.execute(sql,[rec['title'], rec['bloggername'], rec['description'],rec['bloggerlink'],rec['link'],rec['postdate']])
        except:
            for reckey in rec:
                # 해당 문자열에 있는 문자를 제외한 문자를 ' ' 문자로 치환함
                rec[reckey] = re.sub('[^가-힇0-9a-zA-Z<>&.?:/#\[\]\\s]', ' ', rec[reckey])
                dbcursor.execute(sql,[rec['title'], rec['bloggername'], rec['description'],rec['bloggerlink'],rec['link'],rec['postdate']])
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

if __name__ == '__main__':
    main()