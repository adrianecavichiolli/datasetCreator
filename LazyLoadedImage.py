import numpy

class LazyLoadedImage:
    def __init__(self, loader, filename, label, grayscale = False, verbose = False):
        self.loader = loader
        self.filename = filename
        self.label = label
        self.grayscale = grayscale 
        self.verbose = verbose
    
    def getLabel(self):
        return self.label
    
    def getFilename(self):
        return self.filename
    
    def getArray(self):
        if self.verbose:
            print("loading image %s" % self.filename)

        image = self.loader.load()
        if (self.grayscale):
            return image.image.reshape(-1)
        else:
            return numpy.transpose(image.image, (2,0,1)).reshape(-1)
    
    def getShape(self):
        return self.image.shape
    
    def createCopyWithImage(self, newImage):
        return LabeledImage(newImage, self.filename, self.label, self.grayscale)
    
