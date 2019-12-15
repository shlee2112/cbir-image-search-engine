import numpy as np    
import cv2   		   # OpenCV
import imutils         # To check OpenCV version


# Script for extracting color histogram features for each image from the dataset
class ColorDescriptor:

	def __init__(self, bins):

		# Store the number of bins for the HSV color histogram
		self.bins = bins


	# Convert from the RGB color space to the HSV color space. Then, quantify the list of features to represent the image. 
	def describe(self, image):

		# Extract HSV color features from the image dataset
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# Grab the dimensions and compute the center of the image.
		(h,w) = image.shape[:2]
		(cX, cY) = (int(w*0.5)), (int(h*0.5))

		# Then, divide the images into four different segments
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

		(axesX, axesY) = (int(w*0.75) // 2, int(h*0.75) // 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)


		# Constract a mask for each corner of image and extract a color histogram from each image.
		# for (startX, endX, startY, endY) in segments:

		# 	cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
		# 	cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
		# 	cornerMask = cv2.subtract(cornerMask, ellipMask)

		# 	hist = self.histogram(image, cornerMask)
		# 	features.extend(hist)


		hist = self.histogram(image, ellipMask)
		features.extend(hist)

		return features



	def histogram(self, image, mask):

		# Extract a 3D color histogram from the masked region of the image, using the number of bins per channel
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
			[0, 180, 0, 256, 0, 256])

		# Normalize the histogram to obtain scale invarinace
		if imutils.is_cv2():
			hist = cv2.normalize(hist).flatten()
		else:
			hist = cv2.normalize(hist, hist).flatten()


		return hist

