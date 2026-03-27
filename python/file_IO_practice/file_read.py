# file = open('hello.txt','r')    # hello.txt파일을 읽기 모드로 열기
# s = file.read()     # 파일에서 문자열 읽기, readline(), readlines()
# print(s)
# file.close()

with open('hello.txt', 'r') as f:
    # lines = f.readlines()
    # print(lines)

    line = None
    while line != '':
        line = f.readline()
        print(line.strip('\n'))