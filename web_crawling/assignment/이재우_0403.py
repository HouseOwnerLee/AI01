# 1. 저장할 파일명: bugschart_입력날짜.csv 예) bugschart_20260402
# 2. 입력날짜(search_day),랭킹(rank), 가수이름(singer), 곡타이틀(title) 형식으로 파일에 출력한다.
# 3. 입력 가능한 날짜는 2006년09월22일부터 현재날짜 하루전까지이며 입력형식은 다음 예시와 같다. 예) 20260402

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
import time
from datetime import datetime, timedelta

def bugsCrawler(result):
    date1 = datetime.strptime(input('시작 날짜를 입력해주세요: '), "%Y%m%d")
    date2 = datetime.strptime(input('끝 날짜를 입력해주세요: '), "%Y%m%d")
    print("-----------------------------------------------")
    while date1 <= date2:
        # 벅스 URL 등에 활용할 수 있도록 YYYYMMDD 형식으로 변환
        date_str = date1.strftime("%Y%m%d")
        bugsURL = 'https://music.bugs.co.kr/chart/track/day/total?%s' % date1.strftime("%Y%m%d")
        html = urllib.request.urlopen(bugsURL)
        soupBugs = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupBugs.find('tbody')
        for song in tag_tbody.find_all('tr'):
            print(song.find_all('td'))

        # 하루를 더함
        date1 += timedelta(days=1)

    time.sleep(3)


def main():
    result = []
    bugsCrawler(result)

if __name__ == '__main__':
    main()