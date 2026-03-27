code = input("학번 입력: ")
irum = input("이름 입력: ")
kor = int(input("국어 점수 입력: "))
eng = int(input("영어 점수 입력: "))
math = int(input("수학 점수 입력: "))

total = kor + eng + math
average = total / 3

print("\n\t\t\t***성적표***")
print("===========================================")
print("학번   이름   국어  영어  수학  총점  평균")
print("===========================================")
print("%4s %4s %4d %4d %4d %4d %5.2f" % (code,irum,kor,eng,math,total,average))
print("===========================================")