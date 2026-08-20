# 변수에 저장 가능
circle_area = lambda radius, pi: pi * (radius ** 2)
print(circle_area(10, 3.14))

# 일회성으로 바로 사용도 가능
print((lambda radius, pi: pi * (radius ** 2))(3, 3.14))
