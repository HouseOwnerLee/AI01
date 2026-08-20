# os 모듈 : 운영체제에서 제공하는 정보를 제공하거나 운영체제의 기능을 사용할 수 있는 방법을 제공
import os

# print(os.name)
print(os.getcwd()) # 현재 경로
# print(os.path.join(os.getcwd(),'test')) # 현재 경로에 test를 합침
# os.mkdir(os.path.join(os.getcwd(), 'test')) # 현재 경로에 test를 합한 위치에 디렉토리 생성함

# os.rmdir(os.path.join(os.getcwd(),"test")) # 현재 경로/test 디렉토리를 삭제함
# os.remove(os.path.join(os.getcwd(),"test.py")) # 현재 경로에 있는 test.py 파일을 삭제함

os.chdir("C:\\Windows") # "C:\\Windows"로 경로를 변경
print(os.getcwd()) # chdir로 현재 경로가 "C:\\Windows"임
print(os.listdir()) # "C:\\Windows"의 목록을 확인
