lst1 = []
while True:
    lst2 = []

    lst2.append(input("제품코드 입력 => "))
    if lst2[0].lower() == 'exit':
        break
    lst2.append(input("제품명 입력 => "))
    lst2.append(int(input("수량 입력 => ")))
    lst2.append(int(input("단가 입력 => ")))
    lst2.append(lst2[2] * lst2[3])

    lst1.append(lst2)
    print()

total = 0

print("\n\t\t\t *** 제품관리 ***")
print("제품코드    제품명    수량    단가    판매금액")
print("---------------------------------------------")
for lst in lst1:
    print("%4s    %4s    %4d    %4d    %6s" % (lst[0], lst[1], lst[2], lst[3], format(lst[4],',')))
    total += lst[4]
print("---------------------------------------------")
print("총 금액 : %s".rjust(32) % format(total,','))