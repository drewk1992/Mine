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
    cv2.adaptiveThreshold(channel, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 55, 7)
    #mop up the dirt channel, 255, adaptive_method=cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.dilate(channel, close_k, channel)
    cv2.erode(channel, open_k, channel)

def inter_centre_distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

def colliding_circles(circles):
    for index1, circle1 in enumerate(circles):
        for circle2 in circles[index1+1:]:
            x1, y1, Radius1 = circle1[0]
            x2, y2, Radius2 = circle2[0]
            #collision or containment:
            if inter_centre_distance(x1,y1,x2,y2) < Radius1 + Radius2:
                return True

def find_circles(processed, storage, LOW):
    try:
        cv2.HoughCircles(processed, storage, cv2.HOUGH_GRADIENT, 2, 32.0, 30, LOW)#, 0, 100) great to add circle constraint sizes.
    except:
        LOW += 1
        print 'try'
        find_circles(processed, storage, LOW)
    circles = np.asarray(storage)
    print 'number of circles:', len(circles)
    if colliding_circles(circles):
        LOW += 1
        storage = find_circles(processed, storage, LOW)
    print 'c', LOW
    return storage

def draw_circles(storage, output):
    circles = np.asarray(storage)
    print len(circles), 'circles found'
    for circle in circles:
        Radius, x, y = int(circle[0][2]), int(circle[0][0]), int(circle[0][1])
        cv2.Circle(output, (x, y), 1, cv2.RGB(0, 255, 0), -1, 8, 0)
        cv2.Circle(output, (x, y), Radius, cv2.RGB(255, 0, 0), 3, 8, 0)

#split image into RGB components
bbb,ggg,rrr = cv2.split(orig)
#cv2.split(orig,rrr,ggg,bbb,None)
#process each component
channel_processing(rrr)
channel_processing(ggg)
channel_processing(bbb)
#combine images using logical 'And' to avoid saturation
cv2.merge((bbb, ggg, rrr), processed)
cv2.imshow('before canny', processed)
# cv.SaveImage('case3_processed.jpg',processed)
#use canny, as HoughCircles seems to prefer ring like circles to filled ones.
processed = cv2.Canny(processed, 5, 70, 3)
#smooth to reduce noise a bit more
processed = cv2.GaussianBlur(processed, (7, 7), 15)
cv2.imshow('processed', processed)
#find circles, with parameter search
storage = find_circles(processed, storage, 100)
draw_circles(storage, output)
# show images
cv2.imshow("original with circles", output)
cv2.imwrite('case1.jpg',output)

cv2.WaitKey(0)
