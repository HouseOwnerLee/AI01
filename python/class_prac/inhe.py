class A(object): # object 모든 클래스의 원형
    def __init__(self):
        self.aa = 10

    def printA(self):
        print(self.aa)

class B(A):
    def __init__(self):
        super().__init__() # 동등한 표현들 A.__init__(self) # super(B,self).__init__()
        self.bb = 20

    def printB(self):
        print(self.bb)


class C(B):
    def __init__(self):
        super().__init__() # 동등한 표현들 B.__init__(self) # super(C,self).__init__()
        self.cc = 30

    def printC(self):
        print(self.cc)