from 이재우_0306_02 import Sungjuk

lst = []

def menu_title():
    print("*** 성적관리 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")
    print()

def input_sungjuk():
    obj = Sungjuk()
    obj.input_sungjuk()
    obj.process_sungjuk()
    lst.append(obj)
    print("\n성적 입력 성공!!!\n")

def print_sungjuk():
    print("\n\t\t\t *** 성적관리 ***")
    print("________________________________________")
    print("학번  이름  국어  영어  수학  총합  평균  등급")
    print("________________________________________")
    tot_avg = 0
    for obj in lst:
        obj.output_sungjuk()
        tot_avg += obj.avg
    print("________________________________________")
    try:
        print("\t\t\t학생수 : %d, 전체 평균 : %.2f\n" % (len(lst), tot_avg / len(lst)))
    except ZeroDivisionError as e:
        print("\n출력할 성적이 없습니다.", e)
        print()

def search_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음\n")
        return
    hakbun = input("\n조회할 학번 입력 => ")
    for obj in lst:
        if obj.hakbun == hakbun:
            print("\n\t\t\t *** 성적관리 ***")
            print("________________________________________")
            print("학번  이름  국어  영어  수학  총합  평균  등급")
            print("________________________________________")
            obj.output_sungjuk()
            print("________________________________________\n")
            break
    else:
        print("\n조회할 학생이 없습니다.\n")

def update_sungjuk():
    if len(lst) == 0:
        print("\n출력할 데이터가 없음\n")
        return
    hakbun = input("\n수정할 학번 입력 => ")
    for obj in lst:
        if obj.hakbun == hakbun:
            obj.update_sungjuk()
            obj.process_sungjuk()
            print("\n성적 수정 완료!!!\n")
            break
    else:
        print("\n수정할 학생이 없습니다.\n")

def delete_sungjuk():
    hakbun = input("\n삭제할 학번 입력 => ")
    for obj in lst:
        if obj.hakbun == hakbun:
            lst.remove(obj)
            print("\n성적 삭제 완료!!!\n")
            break
    else:
        print("\n삭제할 학생이 없습니다.\n")

if __name__ == "__main__":
    while True:
        menu_title()
        try:
            menu = int(input("메뉴를 선택하세요(1~6) => "))
        except ValueError as e:
            print("\n숫자를 입력해주세요.", e)
            print()
            continue

        if menu == 1:
            input_sungjuk()
        elif menu == 2:
            print_sungjuk()
        elif menu == 3:
            search_sungjuk()
        elif menu == 4:
            update_sungjuk()
        elif menu == 5:
            delete_sungjuk()
        elif menu == 6:
            print("\n프로그램 종료!!")
            break
        else:
            print("\n메뉴를 다시 입력하세요!!\n")
