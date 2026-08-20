dct = {}

dct['code'] = input("제품코드 입력 => ")
dct['name'] = input("제품명 입력 => ")
dct['su'] = int(input("수량 입력 => "))
dct['cost'] = int(input("단가 입력 => "))
dct['total'] = dct['su'] * dct['cost']

print("\n제품코드    제품명    수량    단가    판매금액")
print("---------------------------------------------")
print("%4s    %4s    %4d    %4d    %6d" % (dct['code'], dct['name'], dct['su'], dct['cost'], dct['total']))
print("---------------------------------------------")