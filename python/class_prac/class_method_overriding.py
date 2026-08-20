class Person:
    def greeting(self):
        print('안녕하세요.')

class Student(Person):
    # greeting함수를 재정의함
    def greeting(self):
        super().greeting() # 상위 클래스의 greeting 함수 호출
        print('저는 파이썬 코딩 도장 학생입니다.')

if __name__ == '__main__':
    james = Student()
    james.greeting()