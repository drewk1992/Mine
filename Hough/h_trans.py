import cv2
import matplotlib.pyplot as plt
import numpy as np


def find_mine(img):
    blur = cv2.bilateralFilter(img,9,75,75)
    b, g, r = cv2.split(blur)
    i = b * 2 - r - g
    i = 255 - i
    close_k = np.ones((20, 20), np.uint8)
    open_k = np.ones((10, 10), np.uint8)
    print ("openclosing")
    c = cv2.morphologyEx(i, cv2.MORPH_CLOSE, close_k)
    o = cv2.morphologyEx(c, cv2.MORPH_OPEN, open_k)
    gauss = cv2.GaussianBlur(o, (7, 7), 15)
    print ("gauss")
    rt, th = cv2.threshold(gauss, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print ("thres")
    circles = cv2.HoughCircles(th, cv2.HOUGH_GRADIENT, 1, 2,
                               param1=200, param2=80, minRadius=0, maxRadius=0)
    print ("circ")

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            if i[2] < 20:
                # draw the outer circle
		print ("draw O C")
                cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # draw the center of the circle
		print ("draw i2 C")
                cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
		print ("draw I C")

    plt.imshow(img, cmap='gray')
    plt.show()


if __name__ == '__main__':
    image = cv2.imread('/test.jpg', 	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                )
    find_mine(image)
