import cv2
import numpy as np

win_name = "scanning"
img = cv2.imread("./video/paper.jpg")
# 이미지의 높이와 너비
rows, cols = img.shape[:2]
# 원본 이미지의 점을 스캔본에 표시하지 않기 위해 사용함
draw = img.copy()
# 좌표 카운터
pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

def onMouse(event, x, y, flags, param):
    global pts_cnt
    if event == cv2.EVENT_LBUTTONDOWN:
        # 클릭 지점 표시
        cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
        cv2.imshow(win_name, draw)

        # 클릭한 좌표 저장
        pts[pts_cnt] = [x, y]
        pts_cnt += 1

        # 모서리 4개 선택시
        if pts_cnt == 4:
            print(pts)
            # x + y 값 계산
            sm = pts.sum(axis=1)
            print(sm)
            # y - x 값 계산
            diff = np.diff(pts, axis=1)
            print(diff)

            # x + y가 가장 작으면 좌상단, x + y가 가장 크면 우하단
            topLeft = pts[np.argmin(sm)]
            bottomRight = pts[np.argmax(sm)]
            # y - x가 가장 작으면 우상단, 크면 좌하단
            topRight = pts[np.argmin(diff)]
            bottomLeft = pts[np.argmax(diff)]


            pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])

            # 간격 계산
            w1 = abs(bottomRight[0] - bottomLeft[0])
            w2 = abs(topRight[0] - topLeft[0])
            h1 = abs(topRight[1] - bottomRight[1])
            h2 = abs(topLeft[1] - bottomLeft[1])
            width = int(max([w1,w2]))
            height = int(max([h1, h2]))
            pts2 = np.float32([[0,0], [width - 1,0], [width - 1, height - 1], [0, height - 1]])

            # 이미지 변환
            mtrx = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, mtrx, (width, height))
            cv2.imshow('scanned', result)

cv2.imshow(win_name, img)
cv2.setMouseCallback(win_name, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()