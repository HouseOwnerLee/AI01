import cv2
import numpy as np


## 1. 모델 로드 및 설정
# YOLOv3의 가중치 파일(.weights)과 설정 파일(.cfg)을 불러와 네트워크를 생성
YOLO_net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

classes = []
# 탐지 가능한 사물 이름이 적힌 파일을 읽어 리스트에 저장
with open("yolo.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# 전체 레이어 이름을 가져온 뒤, 출력 레이어(최종 탐지가 이루어지는 층)의 인덱스를 추출
layer_names = YOLO_net.getLayerNames()
output_layers = [layer_names[i-1] for i in YOLO_net.getUnconnectedOutLayers()]
print("******************************")
print(output_layers)
print("******************************")

# 클래스별로 바운딩 박스를 그릴 때 사용할 랜덤 색상을 생성
colors = np.random.uniform(0, 255, size=(len(classes), 3))

## 2. 이미지 전처리
img = cv2.imread("yolo_dog.png") # 분석할 이미지
img = cv2.resize(img, None, fx=1, fy=1) # 이미지 크기를 조절합니다 (현재는 1배율)
height, width, channels = img.shape # 이미지의 높이, 너비, 채널 정보를 저장
print("height, width, channels =>", height, width, channels)
print("---------------------------")
# RGB값 출력
print(img)
print("---------------------------")

# 이미지를 네트워크가 이해할 수 있는 'Blob' 형태로 변환합니다.
# 0.00392는 1/255로 픽셀 값을 0~1 사이로 정규화하며, (416, 416)은 YOLO 모델의 입력 크기
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
YOLO_net.setInput(blob) # 전처리된 Blob을 네트워크의 입력으로 설정
outs = YOLO_net.forward(output_layers) # 네트워크를 실행하여 예측 결과 받아옴
print(outs)

## 3. 탐지 결과 해석
class_ids = [] # 탐지된 사물의 클래스 ID를 담을 리스트
confidences = [] # 탐지된 사물의 확신도(점수)를 담을 리스트
boxes = [] # 탐지된 사물의 좌표 정보를 담을 리스트

for out in outs: # 각 출력 레이어별로 탐지된 정보를 순회
    for detection in out: # 하나의 레이어에서 발견된 수많은 후보군을 확인
        scores = detection[5:] # 데이터의 5번째 이후 요소들이 각 클래스에 대한 확률
        class_id = np.argmax(scores) # 가장 높은 확률을 가진 클래스의 인덱스를 찾음
        confidence = scores[class_id] # 해당 클래스의 확률 값

        # 확신도가 50% 이상만 사물로 인정
        if confidence > 0.5:
            # 탐지된 위치 좌표(0~1 사이 값)를 원래 이미지 크기에 맞게 계산
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            # 사각형의 좌측 상단 꼭짓점 좌표(x, y)를 계산
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])  # 좌표 저장
            confidences.append(float(confidence))  # 확신도 저장
            class_ids.append(class_id)  # 클래스 ID 저장

print(out)
print(out.shape)

## 4. 중복 제거(NMS) 및 시각화
# NMS(Non-Maximum Suppression)를 실행하여 중복된 박스를 제거
indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN # 텍스트를 쓸 폰트 설정
for i in range(len(boxes)):
    if i in indexes: # NMS를 통과한 유효한 박스만 그립니다.
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]]) # 클래스 이름 가져오기
        color = colors[i] # 해당 객체의 색상 선택

        # 이미지 위에 사각형 박스와 레이블 텍스트를 그려줍니다.
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

cv2.imshow("Image", img) # 결과 이미지를 창에 띄웁니다.
cv2.waitKey(0) # 키 입력을 대기합니다.
cv2.destroyAllWindows() # 열린 창을 모두 닫습니다.
