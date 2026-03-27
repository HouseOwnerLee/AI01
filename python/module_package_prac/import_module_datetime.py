# datetime.date() : 연, 월, 일로 날짜를 표현할 때 사용하는 함수
import datetime

day = datetime.date(2021,12,14)
print(day)
print(day.weekday())

# time.time() : UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 반환하는 함수
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 반환
import time
print(time.time())

# time.localtime() : time.time()이 반환한 실숫값을 연,월,일,시,분,초, ... 형태로 바꾸어 주는 함수
print(time.localtime(time.time()))

# time.strftime() : 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공
import time

print(time.strftime('%x', time.localtime(time.time())))
print(time.strftime('%c', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d', time.localtime(time.time())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# datetime 클래스 : 날짜와 시간을 동시에 표현하기 위해서 사용되며, 위에서 다룬 date와 time 클래스에서 지원하는 대부분의 기능을 지원
from datetime import datetime

now = datetime.now()
print("현재 날짜와 시간:", now)
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("포맷된 날짜와 시간:", formatted_date)
print("%s년 %s월 %s일 %s시 %s분 %s초"%(now.year,now.month,now.day,now.hour,now.minute,now.second))

print(datetime(2026, 3, 8, 10, 10, 10,10))
print(datetime(2026, 3, 8))
