import os, csv

if os.path.exists('sangpum_data.csv'):  # 경로상에 해당 파일이 존재하는지 확인
    fp = open('sangpum_data.csv', 'r', encoding='utf-8', newline='')
    reader = list(csv.reader(fp))
    lst = []

    for line in reader:
        dct = {}
        dct["code"] = line[0]
        dct["name"] = line[1]
        dct["su"] = int(line[2])
        dct["cost"] = int(line[3])
        dct["total"] = int(line[4])

        lst.append(dct)

    fp.close()

    total = 0
    print("\n\t\t\t *** 제품관리 ***")
    print("제품코드    제품명    수량    단가    판매금액")
    print("---------------------------------------------")
    for dct in lst:
        print("%4s    %4s    %4d    %4d    %6s"
              % (dct['code'], dct['name'], dct['su'], dct['cost'],format(dct['total'], ',')))
        total += dct['total']
    print("---------------------------------------------")
    print("총 금액 : %s".rjust(34) % format(total, ','))
else:
    print('파일이 존재하지 않습니다!!!')
