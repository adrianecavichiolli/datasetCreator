import cv2

class OpenCVImgReader:
	def __init__(self, imageFactory, fileSystem, openCV = cv2):
		self.cv2 = openCV
		self.imageFactory = imageFactory
		self.fileSystem = fileSystem

	def read(self, path, filename):
		img = self.cv2.imread(self.fileSystem.joinPath(path, filename))
		img[:,:,[0,2]] = img[:,:,[2,0]]
		return self.imageFactory.create(img, filename)