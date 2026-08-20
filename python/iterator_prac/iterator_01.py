# ite = [1, 2, 3]
# ite = {'가':1, '나':2, '다':3}
# ite = {'가', '나', '다'}
ite = "abc" # 반복 가능한 객체

it = ite.__iter__() # 반복 가능한 객체의 이터레이터

print(it.__next__()) # __next__() 메서드 호출로 객체의 요소를 꺼냄
print(it.__next__())
print(it.__next__())
# print(it.__next__()) # 더 꺼낼 요소가 없기 때문에 오류 발생