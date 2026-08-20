import random

if __name__ == '__main__':
    print("로또 당첨 번호 : ",sorted(random.sample(range(1,46),6)))
