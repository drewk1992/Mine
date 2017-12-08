import cv2 #openCV
import exiftool
import numpy as np
import matplotlib.pyplot as plt
import os


exiftoolPath = None
if os.name == 'nt':
    exiftoolPath = 'C:/exiftool/exiftool.exe'
with exiftool.ExifTool(exiftoolPath) as exift:
    print('Exiftool works!')

# Use pyplot to load an example image and display with matplotlib
imageName = cv2.imread('/media/drew/Drew Knight/Thesis/Data/Info/DrewKnight/0017SET/000/IMG_0000_1.tif',0)
imageRaw=plt.imread(imageName).T
plt.imshow(imageRaw.T, cmap='gray')
plt.show()

print('Success! Now you are ready for Part 1 of the tutorial.')
