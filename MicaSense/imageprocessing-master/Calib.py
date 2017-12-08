import numpy as np
import cv2
import micasense.utils as msutils
import micasense.metadata as metadata
import exiftool
import matplotlib.pyplot as plt
import os,glob
import math


exiftoolPath = None
if os.name == 'nt':
    exiftoolPath = 'C:/exiftool/exiftool.exe'

imageRaw = '/mnt/114e4710-77b7-4a37-a8f6-0177deea301b/Desktop/Link to Mine/MicaSense/imageprocessing-master/data/0000SET/000/IMG_0001_3.tif'
meta = metadata.Metadata(imageRaw)
radianceImage, _,_,_,_ = msutils.raw_image_to_radiance(meta, imageRaw)
plotutils.plotwithcolorbar(V,'Vignette Factor')
plotutils.plotwithcolorbar(R,'Row Gradient Factor')
plotutils.plotwithcolorbar(V*R,'Combined Corrections')
plotutils.plotwithcolorbar(L,'Vignette and row gradient corrected raw values')
plotutils.plotwithcolorbar(radianceImage,'All factors applied and scaled to radiance')
