import cv2
import numpy as np

#info of band to cast to
tar = cv2.imread('RE.png',0)
shp = tar.shape
#create cast
cast = np.zeros(shp,np.uint8)
# band to cast
band= cv2.imread('Red.png',0)

for row in range(910):
	for col in range(1229):
		try:
			cast[row,col]=tar[row,col]
		except:
			cast[row,col]=0

cv2.imwrite('Red_cast.png',cast)
