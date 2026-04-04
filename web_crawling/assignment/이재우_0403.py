# 1. 저장할 파일명: bugschart_입력날짜.csv 예) bugschart_20260402
# 2. 입력날짜(search_day),랭킹(rank), 가수이름(singer), 곡타이틀(title) 형식으로 파일에 출력한다.
# 3. 입력 가능한 날짜는 2006년09월22일부터 현재날짜 하루전까지이며 입력형식은 다음 예시와 같다. 예) 20260402

from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
from datetime import datetime, timedelta

class MinDateError(Exception):
    def __init__(self):
        super().__init__("20060922 이상으로 입력하세요.")

class MaxDateError(Exception):
    def __init__(self):
        super().__init__("현재날짜 하루전까지 가능합니다.")

def bugsCrawler(result):
    while True:
        try:
            date1 = datetime.strptime(input('시작 날짜를 입력해주세요: '), "%Y%m%d").date()
            if date1 < datetime(2006, 9, 22).date():
                raise MinDateError()
            if date1 >= datetime.today().date():
                raise MaxDateError()
            break
        except Exception as e:
            print(e)
    while True:
        try:
            date2 = datetime.strptime(input('끝 날짜를 입력해주세요: '), "%Y%m%d").date()
            if date2 < date1:
                raise Exception("시작 날짜 이후 날짜로 입력해주세요.")
            if date2 >= datetime.today().date():
                raise MaxDateError()
            break
        except Exception as e:
            print(e)
    print("-----------------------------------------------")
    while date1 <= date2:
        bugsURL = 'https://music.bugs.co.kr/chart/track/day/total?%s' % date1.strftime("%Y%m%d")
        html = urllib.request.urlopen(bugsURL)
        soupBugs = BeautifulSoup(html, 'html.parser')
        tag_tbody = soupBugs.find('tbody')
        for song in tag_tbody.find_all('tr'):
            attrs = song.find_all('td')
            rank = attrs[1].find('strong').text
            singer = attrs[4].find('a').text
            title = song.find('th').find('a').text
            result.append([date1]+[rank]+[singer]+[title])

        date1 += timedelta(days=1)
    return

def main():
    result = []
    bugsCrawler(result)
    bugs_tbl = pd.DataFrame(result, columns=('입력날짜(search_day)','랭킹(rank)', '가수이름(singer)', '곡타이틀(title)'))
    bugs_tbl.to_csv('bugschart.csv', encoding='utf8', mode='w', index=False)
    del result[:]

if __name__ == '__main__':
    main()