cnt = 0

def input_nums():
    num1 = int(input("첫번째 숫자 입력: "))
    num2 = int(input("두번째 숫자 입력: "))
    print()

    return num1, num2

def min_max_num(num1, num2):
    if num1 > num2:
        min_num = num2
        max_num = num1

    else:
        min_num = num1
        max_num = num2

    return min_num, max_num

def print_primes(min_num, max_num):
    global cnt
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
    return

def print_total():
    if cnt % 10 != 0:
        print()
    print("소수의 갯수 = %d" % cnt)
    return

if __name__ == "__main__":
    num1, num2 = input_nums()
    min_num, max_num = min_max_num(num1, num2)
    print_primes(min_num, max_num)
    print_total()