import csv
import os

# 메뉴 출력하는 함수
def menu_title():
    print("*** 성적관리 ***")
    print("1. 성적정보 입력")
    print("2. 성적정보 출력")
    print("3. 성적정보 조회")
    print("4. 성적정보 수정")
    print("5. 성적정보 삭제")
    print("6. 프로그램 종료")
    print()

# 등급을 반환하는 함수
def get_rank(avg):
    if avg >= 90:
        return "수"
    elif avg >= 80:
        return "우"
    elif avg >= 70:
        return "미"
    elif avg >= 60:
        return "양"
    else:
        return "가"

# 학생 1명의 성적을 입력받는 함수
def input_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv","a",encoding="utf-8",newline="")
        fieldnames = ["code","name","kor","eng","math","total","avg","rank"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
    else:
        fp = open("sungjuk_data.csv","a",encoding="utf-8",newline="")
        fieldnames = ["code","name","kor","eng","math","total","avg","rank"]
        wr = csv.DictWriter(fp, fieldnames=fieldnames)
        # 파일이 존재하지 않으면 헤더를 추가해줌
        wr.writeheader()

    dct = {}
    dct["code"] = input("학번 입력: ")
    dct["name"] = input("이름 입력: ")
    dct["kor"] = int(input("국어 점수 입력: "))
    dct["eng"] = int(input("영어 점수 입력: "))
    dct["math"] = int(input("수학 점수 입력: "))
    dct["total"] = dct["kor"] + dct["eng"] + dct["math"]
    dct["avg"] = dct["total"] / 3
    dct["rank"] = get_rank(dct["avg"])

    # 파일에 학생 정보 쓰기
    wr.writerow(dct)
    fp.close()
    print("\n성적 입력 완료\n")

# 저장된 학생들의 성적을 출력하는 함수
def print_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv","r",encoding="utf-8",newline="")
        lst = list(csv.DictReader(fp))

        # 학생 정보가 없는 경우 출력할 정보가 없으므로 함수 반환
        if not lst:
            print("\n학생 정보가 없음\n")
            fp.close()
            return

        avg_sum = 0
        print("\n\t\t\t***성적표***")
        print("==========================================")
        print("학번   이름   국어  영어  수학  총점  평균  등급")
        print("==========================================")
        for dct in lst:
            print("%4s %4s %4d %4d %4d %4d %5.2f %2s"
                  % (dct["code"], dct["name"],
                     int(dct["kor"]), int(dct["eng"]), int(dct["math"]),
                     int(dct["total"]), float(dct["avg"]), dct["rank"]))
            avg_sum += float(dct["avg"])
        print("==========================================")
        print("\t학생수 : %2d\t\t전체 평균 : %5.2f\n" % (len(lst), avg_sum / len(lst)))
        print()
        fp.close()
    else:
        print("\n출력할 성적 정보가 없음!!!\n")

# 학생 정보 조회하는 함수
def search_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv","r",encoding="utf-8",newline="")
        lst = list(csv.DictReader(fp))

        code = input("\n찾을 학번을 입력하세요 => ")

        for dct in lst:
            if dct["code"] == code:
                print("\n\t\t\t***성적표***")
                print("==========================================")
                print("학번   이름   국어  영어  수학  총점  평균  등급")
                print("==========================================")
                print("%4s %4s %4d %4d %4d %4d %5.2f %2s"
                      % (dct["code"], dct["name"],
                         int(dct["kor"]), int(dct["eng"]), int(dct["math"]),
                         int(dct["total"]), float(dct["avg"]), dct["rank"]))
                print("==========================================\n")
                break
        else:
            print("\n조회할 학생 정보가 없음!!!\n")
        fp.close()
    else:
        print("\n출력할 성적 정보가 없음!!!\n")

# 학생의 성적을 수정하는 함수
def update_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv","r",encoding="utf-8",newline="")
        lst = list(csv.DictReader(fp))

        code = input("\n수정할 학생의 학번 입력: ")
        flag = 0
        for dct in lst:
            if dct["code"] == code:
                dct["kor"] = int(input("국어 점수 입력: "))
                dct["eng"] = int(input("영어 점수 입력: "))
                dct["math"] = int(input("수학 점수 입력: "))
                dct["total"] = dct["kor"] + dct["eng"] + dct["math"]
                dct["avg"] = dct["total"] / 3
                dct["rank"] = get_rank(dct["avg"])
                flag = 1
                break
        else:
            print("\n수정할 학생 정보가 없음!!!\n")
        fp.close()
        if flag == 1:
            fp = open("sungjuk_data.csv","w",encoding="utf-8",newline="")
            wr = csv.DictWriter(fp,fieldnames=["code","name","kor","eng","math","total","avg","rank"])
            wr.writeheader()
            wr.writerows(lst)
            fp.close()
            print("\n학번 %s 수정 완료\n"%code)
    else:
        print("\n성적 정보가 없음!!!\n")

# 학생 정보를 삭제하는 함수
def delete_sungjuk():
    if os.path.exists("sungjuk_data.csv"):
        fp = open("sungjuk_data.csv","r",encoding="utf-8",newline="")
        lst = list(csv.DictReader(fp))

        code = input("\n삭제할 학생의 학번 입력: ")
        flag = 0
        for dct in lst:
            if dct["code"] == code:
                lst.remove(dct)
                print("\n학번 %s 삭제 완료"%code)
                flag = 1
                break
        else:
            print("\n삭제할 학생 정보가 없음!!!\n")
        fp.close()
        if flag == 1:
            fp = open("sungjuk_data.csv","w",encoding="utf-8",newline="")
            wr = csv.DictWriter(fp,fieldnames=["code","name","kor","eng","math","total","avg","rank"])
            wr.writeheader()
            wr.writerows(lst)
            fp.close()

    else:
        print("\n성적 정보가 없음!!!\n")

if __name__ == "__main__":
    while True:
        menu_title()
        menu = int(input("메뉴를 선택하세요(1~6) => "))
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