num1 = int(input("첫번째 숫자 입력: "))
num2 = int(input("두번째 숫자 입력: "))
print()

if num1 > num2:
    num1, num2 = num2, num1

cnt = 0
for num in range(num1, num2 + 1):
    if num < 2:
        continue
    elif num == 2:
        print("%3d" % num, end=' ')
        cnt += 1
        if cnt % 10 == 0:
            print()
    else:
        if num % 2 == 0:
            continue
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                break
        else:
            print("%3d" % num, end=' ')
            cnt += 1
            if cnt % 10 == 0:
                print()

if cnt % 10 != 0:
    print()
print("소수의 갯수 : %d"%cnt)