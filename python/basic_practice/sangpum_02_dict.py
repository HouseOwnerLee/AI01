lst = []

while True:
    dct = {}

    dct['code'] = input("제품코드 입력 => ")
    if dct['code'].lower() == 'exit':
        break
    dct['name'] = input("제품명 입력 => ")
    dct['su'] = int(input("수량 입력 => "))
    dct['cost'] = int(input("단가 입력 => "))
    dct['total'] = dct['su'] * dct['cost']

    lst.append(dct)
    print()

total = 0

print("\n\t\t\t *** 제품관리 ***")
print("제품코드    제품명    수량    단가    판매금액")
print("---------------------------------------------")
for dct in lst:
    print("%4s    %4s    %4d    %4d    %6s" % (dct['code'], dct['name'], dct['su'], dct['cost'], format(dct['total'],',')))
    total += dct['total']
print("---------------------------------------------")
print("총 금액 : %s".rjust(32) % format(total,','))
