with open('hello.txt', 'rt') as file:   # with문이 끝나면 파일을 닫음
    s = file.read()
    print(s)