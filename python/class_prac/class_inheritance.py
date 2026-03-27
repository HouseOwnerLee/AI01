class Person:
    def greeting(self):
        print('안녕하세요.')

# Person 클래스를 상속받음
class Student(Person):
    def study(self):
        print("공부하기")

james = Student()
james.greeting()
james.study()