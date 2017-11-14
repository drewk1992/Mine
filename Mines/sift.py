import cv2
import numpy as np
def img_sift(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    close_k = np.ones((20, 20), np.uint8)
    open_k = np.ones((10, 10), np.uint8)
    c = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, close_k)
    o = cv2.morphologyEx(c, cv2.MORPH_OPEN, open_k)
    gauss = cv2.GaussianBlur(o, (7, 7), 15)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray,None)
    img=cv2.drawKeypoints(gray,kp,cv2.imwrite('sift_keypoints.jpg',img))
    cv2.imwrite('sift_keypoints.jpg',img)
    img=cv2.drawKeypoints(gray,kp,cv2.imwrite('sift_keypoints.jpg',img),flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite('/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Pictures/Thesis/Mines/SiftPoints/sift_keypoints8.jpg',img)

if __name__ == '__main__':
    image = cv2.imread('/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Pictures/Thesis/Mines/IMG_1461.JPG', cv2.IMREAD_ANYCOLOR)
    img_sift(image)
