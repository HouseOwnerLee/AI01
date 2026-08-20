import cv2

src = cv2.imread("./video/cat.jpg", cv2.IMREAD_COLOR)
dst = cv2.blur(src, (9,9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

for ksize in (3,5,7,11):
    # sigmaX : 가우시안 커널의 X축 방향 표준 편차(Standard Deviation)를 의미
    dst = cv2.GaussianBlur(src, (ksize,ksize), 0)
    desc = 'Mean: {}X{}'.format(ksize, ksize)
    cv2.putText(dst, desc, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow("dst", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
