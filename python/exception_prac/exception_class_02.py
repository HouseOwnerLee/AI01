class AgeException(Exception):
    def __init__(self, msg1, msg2):
        self._message1 = msg1
        self.message2 = msg2

def input_age():
    age = int(input("나이를 입력해 주세요: "))

    if age < 0:
        raise AgeException("나이는 음수가 될수 없습니다.", "헐")
    elif age > 150:
        raise AgeException("150세이상 살수 있을까요?","흠")
    else:
        return age

if __name__ == "__main__":
    try:
        age = input_age()
    except AgeException as e:
        print(type(e)) # AgeException 클래스
        print(type(e.args)) # 튜플
        for msg in e.args:
            print(msg)
    else:
        print("나이는 %d세입니다."%age)