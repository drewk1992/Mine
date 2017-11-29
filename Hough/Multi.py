import cv2
import numpy as np

output = cv2.imread('test.jpg', cv2.IMREAD_ANYCOLOR)
orig = cv2.imread('test.jpg', cv2.IMREAD_ANYCOLOR)
h = np.size(orig, 0)
w = np.size(orig, 1)
size = h, w, 3
# create tmp images
bbb = np.zeros((h,w),np.uint8)
ggg = np.zeros((h,w),np.uint8)
rrr = np.zeros((h,w),np.uint8)
processed = np.zeros((h,w) ,np.uint8)
storage = np.zeros(size, dtype=np.float32)
#Create Filters
close_k = np.ones((20, 20), np.uint8)
open_k = np.ones((10, 10), np.uint8)

def channel_processing(channel):
    pass
    c = cv2.morphologyEx(channel, cv2.MORPH_CLOSE, close_k)
    o = cv2.morphologyEx(c, cv2.MORPH_OPEN, open_k)
    gauss = cv2.GaussianBlur(o, (7, 7), 15)
    th = cv2.threshold(gauss, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow("1",th)


bbb,ggg,rrr = cv2.split(orig)
#cv2.split(orig,rrr,ggg,bbb,None)
#process each component
channel_processing(rrr)
channel_processing(ggg)
channel_processing(bbb)


processed = cv2.merge((bbb, ggg, rrr))
cv2.imwrite('combined.jpg', processed)
cv2.imshow("r",rrr)
