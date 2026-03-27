class Person:
    def __init__(self):
        print("Person Class")

    def greeting(self):
        print("안녕하세요")

class University:
    def __init__(self):
        print("University Class")

    def manage_credit(self):
        print('학점 관리')

    def greeting(self):
        print("안녕하세요2")

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

james = Undergraduate()
james.greeting() # 중복되는 함수의 경우 처음 상속받은 상위 클래스의 함수를 호출함
james.manage_credit()
james.study()
