y = [10,20,30]

try:    # 실행할 코드
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    res = y[index] / x

except ZeroDivisionError as e: # try문에서 오류 발생시 처리하는 코드
    print('숫자를 0으로 나눌 수 없습니다.', e)

except IndexError as e:
    print('잘못된 인덱스입니다.', e)

except Exception as e: # 예외 메시지를 변수 e에 받음
    # 모든 에외의 에러 메시지를 출력
    print(e)

else: # 예외가 발생하지 않았을 때 실행할 코드
    print(res)

finally: # 예외 발생 여부와 상관없이 항상 실행할 코드
    print('코드 실행이 끝났습니다.')


















