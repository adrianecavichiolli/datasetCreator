import numpy

class ExtractGridPatches:
    def __init__(self, patchSize):
        self.patchSize = patchSize
    
    def process(self, dataset):
        result = tuple(self.extractGridPatches(data) for data in dataset)
        map(numpy.random.shuffle, result)
        return result
    
    def extractGridPatches(self, data):      
        patches = [self.extractImagePatches(img) for img in data]
        result = [patch for patchList in patches for patch in patchList]
        return result
    
    def extractImagePatches(self, img):
        nPatches = img.image.shape[0] / self.patchSize
        
        return [self.makePatch(img, row, col) 
                    for row in range(nPatches) 
                    for col in range(nPatches)]
    
    def makePatch(self, img, row, col):
        patchSize = self.patchSize
        patch = img.image[row*patchSize:(row+1)*patchSize, col*patchSize:(col+1)*patchSize]
        result =  img.createCopyWithImage(patch)
        return result
