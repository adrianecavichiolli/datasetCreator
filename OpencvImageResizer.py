import cv2

class OpencvImageResizer:
	def resize(self, image, newSize):
		return cv2.resize(image, newSize)