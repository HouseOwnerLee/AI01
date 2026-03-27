class Counter:
    def __init__(self, stop):
        self.current = 0 # 현재 숫자
        self.stop = stop # 반복을 끝낼 숫자

    def __iter__(self):
        return self

    def __next__(self):
        # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
        if self.current < self.stop:
            r = self.current # 현재 숫자를 변수 r에 저장
            self.current += 1 # 현재 숫자를 1 증가시킴
            return r # 숫자 반환
        else:
            # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때 예외
            raise StopIteration

if __name__ == '__main__':
    for i in Counter(3):
        print(i, end=' ')
