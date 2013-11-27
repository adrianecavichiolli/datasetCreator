import numpy

class LabeledImage:
    def __init__(self, image, filename, label, grayscale = False):
        self.image = image
        self.filename = filename
        self.label = label
        self.grayscale = grayscale 
    
    def getLabel(self):
        return self.label
    
    def getFilename(self):
        return self.filename
    
    def getArray(self):
        if (self.grayscale):
            return self.image.reshape(-1)
        else:
            return numpy.transpose(self.image, (2,0,1)).reshape(-1)
    
    def createCopyWithImage(self, newImage):
        return LabeledImage(newImage, self.filename, self.label, self.grayscale)
    
