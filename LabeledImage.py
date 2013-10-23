import numpy

class LabeledImage:
    @staticmethod
    def getLabelFromFilename(filename):
        return int(filename[0:2]) -1
    
    def __init__(self, image, filename, label):
        self.image = image
        self.filename = filename
        self.label = label
    
    def getLabel(self):
        return self.label
    
    def getFilename(self):
        return self.filename
    
    def getArray(self):
        return numpy.transpose(self.image, (2,0,1)).reshape(-1)
    
    def createCopyWithImage(self, newImage):
        return LabeledImage(newImage, self.filename, self.label)
    
