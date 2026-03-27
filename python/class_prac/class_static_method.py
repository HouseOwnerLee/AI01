# 모든 객체가 메서드를 공유함
class Calc:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

print(Calc.add(10, 20))
print(Calc.mul(10, 20))