import cv2
import numpy as np

#load input image
image = cv2.imread('/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Documents/Py_Scripts/HAAR/search.JPG')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
close_k = np.ones((20, 20), np.uint8)
open_k = np.ones((10, 10), np.uint8)
c = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, close_k)
o = cv2.morphologyEx(c, cv2.MORPH_OPEN, open_k)
gauss = cv2.GaussianBlur(o, (7, 7), 15)
#load detector and start it
detector = cv2.CascadeClassifier("/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Documents/Py_Scripts/HAAR/data/cascade.xml")
rects = detector.detectMultiScale(gauss, 10, 10)

# loop over the mines and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(image, "mine #{}".format(i + 1), (x, y - 10),
		cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)

# show the detected mines
cv2.imwrite("detected.jpg", image)
cv2.waitKey(0)
