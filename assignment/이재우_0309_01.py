from 이재우_0309_02 import Sangpum

lst = []

def menu_title():
    print("*** 제품 관리 ***")
    print("1. 제품정보 입력")
    print("2. 제품정보 출력")
    print("3. 제품정보 조회")
    print("4. 제품정보 수정")
    print("5. 제품정보 삭제")
    print("6. 제품정보 종료")
    print()

def input_sangpum():
    obj = Sangpum()
    obj.input_sangpum(lst)
    lst.append(obj)
    print("\n상품 입력 성공!!!\n")

def print_sangpum():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음\n")
        return

    print("\n\t\t\t *** 제품관리 ***")
    print("=============================================")
    print("제품코드   제품명     수량      단가    판매금액")
    print("=============================================")
    total = 0
    for obj in lst:
        total += int(obj.kumack)
        obj.output_sangpum()
    print("=============================================")
    print("\t\t\t\t\t\t 총금액 : %7d\n" % total)

def search_sangpum():
    if len(lst) == 0:
        print("\n데이터가 없음\n")
        return

    code = input("\n조회할 제품코드 입력 => ")

    for obj in lst:
        if obj.code == code:
            print("\n\t\t\t *** 제품관리 ***")
            print("=============================================")
            print("제품코드   제품명     수량      단가    판매금액")
            print("=============================================")
            obj.output_sangpum()
            print("=============================================\n")
            break
    else:
        print("\n조회할 제품이 없습니다.\n")

def update_sangpum():
    if len(lst) == 0:
        print("\n데이터가 없음\n")
        return

    code = input("\n수정할 제품코드 입력 => ")

    for obj in lst:
        if obj.code == code:
            obj.update_sangpum()
            obj.process_sangpum()
            print("\n제품 수정 완료!!!\n")
            break
    else:
        print("\n수정할 제품이 없습니다.\n")

def delete_sangpum():
    if len(lst) == 0:
        print("\n데이터가 없음\n")
        return

    code = input("\n삭제할 제품코드 입력 => ")

    for obj in lst:
        if obj.code == code:
            lst.remove(obj)
            print("\n제품 삭제 완료!!!\n")
            break
    else:
        print("\n삭제할 제품이 없습니다.\n")

if __name__ == "__main__":
    while True:
        menu_title()
        try:
            menu = int(input("메뉴를 선택하세요(1~6) => "))
        except ValueError as e:
            print("\n숫자를 입력해주세요.\n")
            continue

        if menu == 1:
            input_sangpum()
        elif menu == 2:
            print_sangpum()
        elif menu == 3:
            search_sangpum()
        elif menu == 4:
            update_sangpum()
        elif menu == 5:
            delete_sangpum()
        elif menu == 6:
            print("\n프로그램 종료!!")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")
