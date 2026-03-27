lst = []

lst.append(input("제품코드 입력 => "))
lst.append(input("제품명 입력 => "))
lst.append(int(input("수량 입력 => ")))
lst.append(int(input("단가 입력 => ")))
lst.append(lst[2] * lst[3])

print("\n제품코드    제품명    수량    단가    판매금액")
print("---------------------------------------------")
print("%4s    %4s    %4d    %4d    %6d" % (lst[0], lst[1], lst[2], lst[3], lst[4]))
print("---------------------------------------------")