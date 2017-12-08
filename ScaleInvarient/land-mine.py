import cv2
import matplotlib.pyplot as plt
import numpy as np
import cv2



def find_mine(img):
    blur = cv2.bilateralFilter(img,9,75,75)
    b, g, r = cv2.split(blur)
    i = b * 2 - r - g
    i = 255 - i
    close_k = np.ones((20, 20), np.uint8)
    open_k = np.ones((10, 10), np.uint8)
    c = cv2.morphologyEx(i, cv2.MORPH_CLOSE, close_k)
    o = cv2.morphologyEx(c, cv2.MORPH_OPEN, open_k)
    gauss = cv2.GaussianBlur(o, (7, 7), 15)
    rt, th = cv2.threshold(gauss, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    circles = cv2.HoughCircles(th, cv2.HOUGH_GRADIENT, 1, 2,
                               param1=500, param2=15, minRadius=0, maxRadius=0)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            if i[2] < 20:
                # draw the outer circle
                cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
                cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    plt.imshow(img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    image = cv2.imread('/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Pictures/DJI_0018.JPG', cv2.IMREAD_ANYCOLOR)
    find_mine(image)
