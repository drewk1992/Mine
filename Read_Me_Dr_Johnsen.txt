Calib_files
	Contains images clipped to image calibration for each band as well as image reflectance 	values
HAAR
	Neg.py - Downloads negative images from image net and removes bad images. Creates custom 		cascade classifier uses neg + mine.png to create positives, neg for the negatives
	
	cascadeClass.py - Runs HARR Classification using previously created cascade classifier
Hough
	addpted.py- used to preform canny edge detection
	rest is experimental and probably doesnt work

Mines

MicaSense
	This software was created by Micasense the company that creates the 5 band sensor used to 		calibrate cameras.  Unfortunatly there is no good documentation and I got stuck trying to 		update their tutorial data for my use.  Will come back to this later on I think this could 		be incorperated in a machine vision approach.

Raw images
	contains raw images of 5 band MicaSense RedEdge Sensor
	ImAlign.py Used to allign images using OpenCV motion detection
	ReCast.py used to trim images to smallest sized image
	ImAlign2.py Not fully working will allign images and take into account Image Gradient
	Get_Gradient is used by ImAlign2.py

	Trimmed Folder- Contains the results of image alignment and composite

Scaleinvarient	
	sift.py- used to create sift tie points on mine image
