class A:
    def __init__(self, x):
        self.aa = x

    def printA(self):
        print(self.aa)

class B(A):
    def __init__(self, x, y):
        # 상위 클래스에 인자 전달
        super().__init__(x) # 동등한 표현들 A.__init__(self, x) # super(B,self).__init__(x)
        self.bb = y

    def printB(self):
        print(self.bb)


class C(B):
    def __init__(self, x, y, z):
        # 상위 클래스에 인자 전달가능
        super().__init__(x, y) # 동등한 표현들 B.__init__(self, x, y) # super(C,self).__init__(x, y)
        self.cc = z

    def printC(self):
        print(self.cc)