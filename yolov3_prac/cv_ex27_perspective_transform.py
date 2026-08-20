import cv2
import numpy as np

filename = "./video/fish.jpg"
img = cv2.imread(filename)
# 이미지의 높이와 너비
rows, cols = img.shape[:2]

# 원본 좌표
pts1 = np.float32([[0,0],[0,rows], [cols,0], [cols,rows]])
# 이미지가 변형된 후 원본 좌표가 놓일 위치
pts2 = np.float32([[100,50], [10, rows-50], [cols-100,50],[cols-10, rows-50]])

# 모서리에 시각적 표시
cv2.circle(img, (0,0), 10, (255,0,0), -1) # 좌상
cv2.circle(img, (0,rows), 10, (0,255,0), -1) # 우상
cv2.circle(img, (cols,0), 10, (0,0,255), -1) # 좌하
cv2.circle(img, (cols,rows), 10, (0,255,255), -1) # 우하

# 변환 행렬 게산
mtrx = cv2.getPerspectiveTransform(pts1, pts2)
print(mtrx)
# 이미지 변환
dst = cv2.warpPerspective(img, mtrx, (cols,rows))

cv2.imshow("origin", img)
cv2.imshow("perspective", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()