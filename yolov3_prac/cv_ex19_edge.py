import cv2

src = cv2.imread("./video/moments.jpg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)
canny = cv2.Canny(src, 150, 255)

sobel = cv2.resize(sobel, dsize=(800,600), interpolation=cv2.INTER_AREA)
laplacian = cv2.resize(laplacian, dsize=(800,600), interpolation=cv2.INTER_AREA)
canny = cv2.resize(canny, dsize=(800,600), interpolation=cv2.INTER_AREA)

cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.imshow("canny", canny)
cv2.waitKey()
cv2.destroyAllWindows()