def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    # for문으로 구현 가능
    # result = 1
    # for i in range(n, 0, -1):
    #     result *= i
    # return result

print(factorial(5))