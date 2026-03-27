# 접근제한자
# -파이썬은 자바나 C++처럼 명시적으로 public, protected, private과 같은 키워드를 사용하지 않는 대신 밑줄(_)을 사용해서 접근제한을 구분한다.
# -밑줄이 없는 경우는 public 처럼 객체 생성 후 누구나 외부에서 직접 접근이 가능하다.
# -밑줄(_)이 하나인 경우는 비공개모드로서 직접적인 접근을 제한하고 있어 객체 생성 후 외부에서 직접 접근을 해서는 안된다. 하지만 접근을 시도하면 오류없이 접근은 가능하다.
# -밑줄(_)이 두개인 경우는 객체 생성후 외부에서 직접적인 접근을 할 수 없으며 객체 생성 후 직접 접근을 시도하면 정의되지 않은 속성이나 메서드라고 오류메시지가 발생한다.
# -밑줄(_)이 두개인 경우는 객체 내부에서는 접근이 가능하며 자식클래스에게 상속이 되지 않는다.

class Person:
    def __init__(self, name, age, address, wallet):
        self._name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_wallet(self):
        return self.__wallet

    def set_wallet(self, wallet):
        self.__wallet = wallet

    wallet = property(get_wallet, set_wallet)

    def pay(self, amount):
        self.__wallet -= amount
        print("이제 %d원 남았네요." % self.__wallet)

if __name__ == '__main__':
    maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
    print(maria.name)
    maria.name = "이기자"
    print(maria.name)
    print(maria.wallet)
    maria.wallet = 20000
    print(maria.wallet)