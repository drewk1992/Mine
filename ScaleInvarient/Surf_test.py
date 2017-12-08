
import cv2
import numpy as np

surf = cv2.xfeatures2d.SURF_create(400)
#example
train = cv2.imread('/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Pictures/Thesis/Mines/Grass/DJI_0011.JPG',0)
#real
test= cv2.imread('/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Pictures/Thesis/Mines/Grass/DJI_0018.JPG',0)

# Find Descriptors
kp1,trainDes1 = surf.detectAndCompute(train, None)
kp2,testDes2  = surf.detectAndCompute(test, None)

# Create BFMatcher and add cluster of training images. One for now.
bf = cv2.BFMatcher(cv2.NORM_L1,crossCheck=False) # crossCheck not supported by BFMatcher
clusters = np.array([trainDes1])
bf.add(clusters)

# Train: Does nothing for BruteForceMatcher though.
bf.train()

matches = bf.match(testDes2)
matches = sorted(matches, key = lambda x:x.distance)

# Since, we have index of only one training image,
# all matches will have imgIdx set to 0.
for i in range(len(matches)):
    print matches[i].imgIdx
