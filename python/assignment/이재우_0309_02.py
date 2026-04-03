class SameCodeError(Exception):
    def __init__(self):
        super().__init__("\n중복된 제품코드입니다.\n")

class NameError(Exception):
    def __init__(self):
        super().__init__("\n문자만 입력가능합니다.\n")

class Sangpum:
    def __init__ (self):
        self._code = ""
        self._name = ""
        self._su = 0
        self._price = 0
        self._kumack = 0

    def get_code(self):
        return self._code
    def set_code(self, code):
        self._code = code
    code = property(get_code, set_code)

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name = property(get_name, set_name)

    def get_su(self):
        return self._su
    def set_su(self, su):
        self._su = su
    su = property(get_su, set_su)

    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
    price = property(get_price, set_price)

    def get_kumack(self):
        return self._kumack
    def set_kumack(self, kumack):
        self._kumack = kumack
    kumack = property(get_kumack, set_kumack)

    def input_sangpum(self, lst):
        while True:
            try:
                self._code = input("상품코드 입력 : ")
                if self._code.isdigit():
                    raise NameError

                for obj in lst:
                    if self._code == obj.code:
                        raise SameCodeError
                else:
                    break
            except Exception as e:
                print(e)
        while True:
            try:
                self._name = input("상품이름 입력 : ")
                if self._name.isdigit():
                    raise NameError
                else:
                    break
            except Exception as e:
                print(e)
        self.update_sangpum()

    def process_sangpum(self):
        self._kumack = self._su * self._price
        
    def output_sangpum(self):
        print("%4s    %4s    %4d   %7d %10d" %
              (self._code, self._name, int(self._su), int(self._price), int(self._kumack)))

    def update_sangpum(self):
        while True:
            try:
                self._su = int(input("상품수량 입력 : "))
                break
            except ValueError:
                print("\n숫자를 입력해주세요.\n")
        while True:
            try:
                self._price = int(input("상품단가 입력 : "))
                break
            except ValueError:
                print("\n숫자를 입력해주세요.\n")
        self.process_sangpum()