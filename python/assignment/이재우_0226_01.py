students = []
while True:
    dct = {}
    dct['code'] = input("학번 입력: ")
    if dct['code'].lower() == 'exit':
        break
    dct['name'] = input("이름 입력: ")
    dct['kor'] = int(input("국어 점수 입력: "))
    dct['eng'] = int(input("영어 점수 입력: "))
    dct['math'] = int(input("수학 점수 입력: "))
    dct['total'] = dct['kor'] + dct['eng'] + dct['math']
    dct['avg'] = dct['total'] / 3

    students.append(dct)
    print()

avg = 0
print("\n\t\t\t***성적표***")
print("=====================================")
print("학번   이름   국어  영어  수학  총점  평균")
print("=====================================")
for dct in students:
    print("%4s %4s %4d %4d %4d %4d %5.2f"
      % (dct['code'], dct['name'], dct['kor'], dct['eng'], dct['math'], dct['total'], dct['avg']))
    avg += dct['avg']
print("=====================================")
print("\t학생수 : %2d\t\t전체 평균 : %5.2f" %(len(students), avg / len(students)))