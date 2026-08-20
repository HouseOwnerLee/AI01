import numpy as np
import cv2

src = cv2.imread("./video/zebra.jpg")

# 구조화 요소(커널 행렬)를 생성하는 함수
# shape: cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (9,9))
print(kernel)

# 팽창 연산 -> 흰색 영역을 확장
dilate = cv2.dilate(src, kernel, anchor=(-1, -1), iterations = 5)
# 침식 연산 -> 흰색 영역을 깍아냄
erode = cv2.erode(src, kernel, anchor=(-1,-1), iterations = 5)

# 3개 이미지 합침
dst = np.concatenate((src, dilate, erode), axis=1)
dst_re = cv2.resize(dst, dsize=(0,0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
cv2.imshow("dst", dst_re)
cv2.waitKey(0)
cv2.destroyAllWindows()