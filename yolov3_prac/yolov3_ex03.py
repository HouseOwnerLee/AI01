import cv2
import numpy as np

VideoSignal = cv2.VideoCapture('video/youquiz4.mp4')

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

while True:
    ret, frame = VideoSignal.read()
    h, w, c = frame.shape

    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    YOLO_net.setInput(blob)  # 전처리된 Blob을 네트워크의 입력으로 설정
    outs = YOLO_net.forward(output_layers)  # 네트워크를 실행하여 예측 결과 받아옴

    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * w)
                center_y = int(detection[1] * h)
                dw = int(detection[2] * w)
                dh = int(detection[3] * h)

                x = int(center_x - dw / 2)
                y = int(center_y - dh / 2)
                boxes.append([x, y, dw, dh])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    ## 4. 중복 제거(NMS) 및 시각화
    # NMS(Non-Maximum Suppression)를 실행하여 중복된 박스를 제거
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    for i in range(len(boxes)):
        if i in indexes:  # NMS를 통과한 유효한 박스만 그립니다.
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])  # 클래스 이름 가져오기
            score = confidences[i]

            # 이미지 위에 사각형 박스와 레이블 텍스트를 그려줍니다.
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)
            cv2.putText(frame, label, (x, y - 20), cv2.FONT_ITALIC, 0.5, (255, 255, 255), 1)

    cv2.imshow("YOLOv3", frame)  # 결과 이미지를 창에 띄웁니다.

    if cv2.waitKey(100) > 0:
        break


