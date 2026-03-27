# chr() : 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환하는 함수
print(chr(97))
print(chr(65))
print(chr(48))

# ord() : 문자의 유니코드 숫자 값을 반환하는 함수
print(ord('a'))
print(ord('A'))
print(ord('0'))

# dir() : 객체가 지닌 변수나 함수를 보여주는 함수
print(dir([1,2,3]))
print("--------------------------------")
print(dir({1:'a'}))

# enumerate() : 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 반환
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

print('_________________________________')
for val in enumerate(['body', 'foo', 'bar']):
    print(val)

# map() : 입력받은 데이터의 각 요소에 함수를 적용한 결과를 반환하는 함수
def two_times(x):
    return x * 2

print(list(map(two_times, [1,2,3,4])))

# max(), min() : 최대,최솟값을 반환하는 함수
print(max([1,2,3,4]))
print(min([1,2,3,4]))

# round() : 수자를 입력받아 반올림해 반환하는 함수
print(round(4.6))
print(round(4.2))
print(round(-4.6))
print(round(-4.2))

# sorted() : 입력 데이터를 정렬한 후 그 결과를 리스트로 반환하는 함수
print(sorted([2,3,1,4]))
print(sorted(['a','c','d','b']))
print(sorted("zero"))
print(sorted([2,3,1,4], reverse=True))

countries = [
    {'code': 'KR', 'name': 'Korea'},
    {'code': 'CA', 'name': 'Canada'},
    {'code': 'US', 'name': 'United States'},
    {'code': 'GB', 'name': 'United Kingdom'},
    {'code': 'CN', 'name': 'China'}
]

print(sorted(countries, key=lambda country: country['code']))
print(sorted(countries, key=lambda country: country['name'], reverse=True))

my_list = [-5, 3, -1, 0, 2, -4]
print(sorted(my_list, key=abs, reverse=True))

my_list = ["api", "app", "carrier", "demon", "aaa"]
print(sorted(my_list, key=len))

# sum() : 입력 데이터의 합을 반환하는 함수
print(sum([1,2,3]))

# zip() : 동일한 개수로 이루어진 데이터들을 묶어서 반환하는 함수
print(list(zip([1,2,3], [4,5,6])))
print(list(zip("abc", "def")))

for item in zip("abc", "def"):
    print(item)

for x, y in zip("abc", [1,2,3]):
    print(x, y)