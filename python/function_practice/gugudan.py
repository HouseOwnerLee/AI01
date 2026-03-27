def input_num():
    num1 = int(input("첫번째 숫자를 입력하시오: "))
    num2 = int(input("두번째 숫자를 입력하시오: "))
    return num1, num2

def min_max_num(num1, num2):
    if num1 > num2:
        min_num = num2
        max_num = num1

    else:
        min_num = num1
        max_num = num2

    return min_num, max_num

def proc_gugudan(min_num, max_num):
    for dan in range(min_num, max_num + 1):
        print("** %d단 **"%dan, end="\t")
    print()

    for i in range(1,10):
        for dan in range(min_num, max_num + 1):
            print("%d * %d = %2d"%(dan,i,i*dan),end='\t')
        print()

    return

if __name__ == "__main__":
    num1, num2 = input_num()
    min_num, max_num = min_max_num(num1, num2)
    proc_gugudan(min_num, max_num)
