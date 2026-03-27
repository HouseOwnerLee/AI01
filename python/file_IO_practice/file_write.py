# file = open('hello.txt', 'wt')
# file.write('Hello Python!')     # 파일에 쓰기
# file.close()

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

with open('hello.txt', 'w') as f:
    # for i in range(3):
    #     f.write('Hello, World! {0}\n'.format(i))
    f.writelines(lines)