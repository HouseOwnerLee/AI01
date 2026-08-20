import csv
import os

def menu_title():
    print("*** 제품 관리 ***")
    print("1. 제품정보 입력")
    print("2. 제품정보 출력")
    print("3. 제품정보 조회")
    print("4. 제품정보 수정")
    print("5. 제품정보 삭제")
    print("6. 제품정보 종료")
    print()

def input_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "at", encoding="utf-8", newline="")
        fieldnames = ["code", "irum", "su", "price", "kumack"]
        wr = csv.DictWriter(fp, fieldnames = fieldnames)
    else:
        fp = open("sangpum_data.csv", "at", encoding="utf-8", newline="")
        fieldnames = ["code", "irum", "su", "price", "kumack"]
        wr = csv.DictWriter(fp, fieldnames = fieldnames)
        wr.writeheader()

    dct = {}
    dct["code"] = input("제품코드 입력 => ")
    dct["irum"] = input("제품명 입력 => ")
    dct["su"] = int(input("수량 입력 => "))
    dct["price"] = int(input("단가 입력 => "))
    dct["kumack"] = dct["su"] * dct["price"]
    wr.writerow(dct)
    fp.close()
    print("\n제품정보 입력 성공!!\n")

def print_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="utf-8", newline="")
        lst = list(csv.DictReader(fp))

        print("\n\t\t\t *** 제품관리 ***")
        print("=============================================")
        print("제품코드   제품명     수량      단가    판매금액")
        print("=============================================")
        total = 0
        for data in lst:
            total += int(data["kumack"])
            print("%4s     %4s    %4d    %4d    %6d" %
                  (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
        print("=============================================")
        print("\t\t\t\t\t\t 총금액 : %7d\n" % total)

        fp.close()
    else:
        print("\n출력할 제품 정보가 없음!!!\n")

def search_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="utf-8", newline="")
        lst = list(csv.DictReader(fp))
        code = input("\n조회할 제품코드 입력 => ")

        for data in lst:
            if data["code"] == code:
                print("\n=============================================")
                print("제품코드   제품명     수량      단가    판매금액")
                print("=============================================")
                print("%4s     %4s    %4d    %4d    %6d" %
                      (data["code"], data["irum"], int(data["su"]), int(data["price"]), int(data["kumack"])))
                print("=============================================\n")
                break
        else:
            print("\n조회할 제품 정보가 없음!!!\n")
        fp.close()
    else:
        print("\n출력할 제품 정보가 없음!!!\n")

def update_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="utf-8", newline="")
        lst = list(csv.DictReader(fp))
        code = input("\n수정할 제품코드 입력 => ")
        flag = 0
        for data in lst:
            if data["code"] == code:
                data["su"] = int(input("수량 입력 => "))
                data["price"] = int(input("단가 입력 => "))
                data["kumack"] = data["su"] * data["price"]
                flag = 1
                break
        else:
            print("\n수정할 제품 정보가 없음!!!\n")

        fp.close()
        if flag == 1:
            fp2 = open("sangpum_data.csv", "w", encoding="utf-8", newline="")
            wr = csv.DictWriter(fp2, fieldnames=["code", "irum", "su", "price", "kumack"])
            wr.writeheader()
            wr.writerows(lst)
            print("\n제품 코드 %s 수정 완료\n"%code)
            fp2.close()
    else:
        print("\n제품 정보가 없음!!!\n")

def delete_data():
    if os.path.exists("sangpum_data.csv"):
        fp = open("sangpum_data.csv", "r", encoding="utf-8", newline="")
        lst = list(csv.DictReader(fp))
        code = input("\n삭제할 제품코드 입력 => ")
        flag = 0
        for data in lst:
            if data["code"] == code:
                lst.remove(data)
                print("\n제품정보 삭제 성공\n")
                flag = 1
                break
        else:
            print("\n삭제할 제품 정보가 없음!!!\n")

        fp.close()

        if flag == 1:
            fp2 = open("sangpum_data.csv", "w", encoding="utf-8", newline="")
            wr = csv.DictWriter(fp2, fieldnames=["code", "irum", "su", "price", "kumack"])
            wr.writeheader()
            wr.writerows(lst)
            fp2.close()

    else:
        print("\n제품 정보가 없음!!!\n")

if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("메뉴를 선택하세요(1~6) =>"))
        if menu == 1:
            input_data()
        elif menu == 2:
            print_data()
        elif menu == 3:
            search_data()
        elif menu == 4:
            update_data()
        elif menu == 5:
            delete_data()
        elif menu == 6:
            print("\n프로그램 종료!!")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")