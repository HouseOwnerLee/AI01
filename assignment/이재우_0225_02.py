num1 = int(input("첫번째 숫자를 입력하시오: "))
num2 = int(input("두번째 숫자를 입력하시오: "))

if num1 > num2:
    num1, num2 = num2, num1

for dan in range(num1, num2 + 1):
    print("\n** %d단 **"%dan)

    for i in range(1,10):
        print("%d * %d = %2d"%(dan,i,i*dan))