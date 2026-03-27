from abc import *

# 추상 클래스
class StudentBase(metaclass = ABCMeta):
    # 추상 메서드, 이 클래스를 상속받는 하위 클래스는 이 메서드를 정의해야함(아닐 경우 오류 발생)
    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def go_to_school(self):
        pass

class Student(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("학교가기")

class Children(StudentBase):
    def study(self):
        print("공부하기")

    def go_to_school(self):
        print("유치원 가기")

if __name__ == '__main__':
    james = Student()
    james.study()
    james.go_to_school()
    print("----------------")
    obj = Children()
    obj.study()
    obj.go_to_school()
    print("----------------")
    lst = []
    lst.append(james)
    lst.append(obj)
    for data in lst:
        data.study()
        data.go_to_school()