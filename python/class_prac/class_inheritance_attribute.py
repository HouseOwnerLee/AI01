class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = "안녕하세요."

class Student(Person):
    def __init__(self):
        # 상위클래스의 __init__ 메서드를 호출함
        super().__init__()
        print('Student __init__')
        self.school = '파이썬 코딩 도장'

class Student2(Person):
    # __init__ 메서드가 없다면 기반 클래스의 __init__이 자동으로 호출됨
    pass

if __name__ == '__main__':
    james = Student()
    print(james.school)
    print(james.hello)

    maria = Student2()
    print(maria.hello)