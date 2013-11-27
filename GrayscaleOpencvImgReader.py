import cv2

class GrayscaleOpenCVImgReader:
    def __init__(self, imageFactory, fileSystem, openCV = cv2):
        self.cv2 = openCV
        self.imageFactory = imageFactory
        self.fileSystem = fileSystem

    def read(self, path, filename):
        img = self.cv2.imread(self.fileSystem.joinPath(path, filename), self.cv2.CV_LOAD_IMAGE_GRAYSCALE)
        return self.imageFactory.create(img, filename)
    
