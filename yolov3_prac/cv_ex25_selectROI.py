import cv2

img = cv2.imread('./video/sunset.jpg')
x, y, w, h = cv2.selectROI('img', img, False)
print(x, y, w, h)

if w and h:
    roi = img[y:y+h, x:x+w]
    cv2.imshow('cropped', roi)
    cv2.moveWindow('cropped', 0, 0)
    cv2.imwrite('./video/cropped2111.jpg', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()