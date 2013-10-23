import unittest
from ExtractGridPatches import ExtractGridPatches
from mock import Mock
import numpy
from LabeledImage import LabeledImage
from TestUtils import arrayEqualsTo

class testExtractGridPatches(unittest.TestCase):
    def test_all(self):
        target = ExtractGridPatches(patchSize = 4)
        
        trainImages, trainExpected = self.makeRandomImageExpectedPair(numImages = 60, imgSize = 4, numPatches = 9)
        validImages, validExpected = self.makeRandomImageExpectedPair(numImages = 10,imgSize = 4, numPatches = 9)
        testImages, testExpected = self.makeRandomImageExpectedPair(numImages = 10,imgSize = 4, numPatches = 9)

        expected = (trainExpected, validExpected, testExpected)
        result = target.process((trainImages, validImages, testImages))
        
        expectedImages = tuple(self.getImages(dataset) for dataset in expected)
        resultImages = tuple(self.getImages(dataset) for dataset in result)

        [numpy.testing.assert_array_equal(expectedImages[i], resultImages[i]) for i in range(3)]

    
    def getImages(self, dataset):
        return numpy.sort(numpy.asarray([img.image for img in dataset]), axis=0)

    def makeRandomImageExpectedPair(self, numImages, imgSize, numPatches):
        patches = [[self.makeRandomImage((4,4)) for i in range(numPatches)] for i in range(numImages)]
        images = [self.joinPatches(patchList) for patchList in patches]
        return images, [patch for patchList in patches for patch in patchList]
  
    def makeRandomImage(self, size):
        return LabeledImage(numpy.random.rand(*size), '', 0)
        
    
    def joinPatches(self, patchList):
        nPatches = int(numpy.sqrt(len(patchList)))
        patchSize = patchList[0].image.shape[0]
        
        dim = nPatches * patchSize
        image = numpy.zeros((dim,dim))
        
        for i in range(nPatches):
            for j in range(nPatches):
                image[i*patchSize:(i+1)*patchSize, j*patchSize:(j+1)*patchSize] = patchList[i*nPatches + j].image
        
        return LabeledImage(image, '', 0)