# 제품코드, 제품명, 수량, 단가를 입력받아 금액을 계산하여 출력하는 프로그램
# 입력 받은 데이터는 sangpum_data.txt에 csv형식으로 저장

fp = open('sangpum_data.txt', 'w', encoding='utf-8') # w:쓰기, r:읽기, a:추가, b:바이너리
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
    fp.write(dct['code'] + ',' + dct['name'] + ',' + str(dct['su']) + ',' + str(dct['cost']) + '\n')
    print()

fp.close()
total = 0
print("\n\t\t\t *** 제품관리 ***")
print("제품코드    제품명    수량    단가    판매금액")
print("---------------------------------------------")
for dct in lst:
    print("%4s    %4s    %4d    %4d    %6s" % (dct['code'], dct['name'], dct['su'], dct['cost'], format(dct['total'],',')))
    total += dct['total']
print("---------------------------------------------")
print("총 금액 : %s".rjust(32) % format(total,','))