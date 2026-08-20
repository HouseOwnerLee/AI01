import cv2

src = cv2.imread('./video/tomato.jpg', cv2.IMREAD_COLOR)
src = cv2.resize(src, None, fx=1/3, fy=1/3, interpolation=cv2.INTER_AREA)
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

cv2.imshow('src', src)
cv2.imshow('hsv', hsv)
cv2.imshow('h', h)
cv2.imshow('s', s)
cv2.imshow('v', v)
cv2.waitKey()
cv2.destroyAllWindows()
