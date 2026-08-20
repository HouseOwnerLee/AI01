class Counter:
    def __init__(self, stop):
        self.stop = stop

    # __getitem__만 구현해도 이터레이터가 됨, __iter__, __next__ 생략 가능
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError

if __name__ == '__main__':
    print(Counter(3)[0], Counter(3)[1], Counter(3)[2])

    for i in Counter(3):
        print(i, end=' ')