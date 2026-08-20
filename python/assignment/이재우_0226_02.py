students = []
while True:
    lst = []
    lst.append(input("학번 입력: "))
    if lst[0].lower() == 'exit':
        break
    lst.append(input("이름 입력: "))
    lst.append(int(input("국어 점수 입력: ")))
    lst.append(int(input("영어 점수 입력: ")))
    lst.append(int(input("수학 점수 입력: ")))
    lst.append(lst[2] + lst[3] + lst[4])
    lst.append(lst[5] / 3)

    students.append(lst)
    print()

avg = 0
print("\n\t\t\t***성적표***")
print("=====================================")
print("학번   이름   국어  영어  수학  총점  평균")
print("=====================================")
for lst in students:
    print("%4s %4s %4d %4d %4d %4d %5.2f"
      % (lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6]))
    avg += lst[6]
print("=====================================")
print("\t학생수 : %2d\t\t전체 평균 : %5.2f" %(len(students), avg / len(students)))