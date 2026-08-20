import cv2

src = cv2.imread("./video/chess.jpg", cv2.IMREAD_COLOR)

# 복사
dst = src.copy()
# 관심 영역
roi = src[100:600, 200:700]
# 좌측 상단에 관심 영역 삽입
dst[0:500, 0:500] = roi

src = cv2.resize(src, None, fx=1/4, fy=1/4, interpolation=cv2.INTER_AREA)
dst = cv2.resize(dst, None, fx=1/4, fy=1/4, interpolation=cv2.INTER_AREA)
cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()