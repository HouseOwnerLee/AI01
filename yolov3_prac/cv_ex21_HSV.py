import cv2

src = cv2.imread('./video/tomato.jpg', cv2.IMREAD_COLOR)
src = cv2.resize(src, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

# 입력 이미지, 낮은 범위, 높은 범위 >> 입력 이미지에서 낮은 범위에서 높은 범위 사이의 요소를 추출
h = cv2.inRange(h, 8, 20)
orange = cv2.bitwise_and(hsv, hsv, mask=h)
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)

cv2.imshow('src', src)
cv2.imshow('orange', orange)
cv2.waitKey()
cv2.destroyAllWindows()