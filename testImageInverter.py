import unittest
from ImageInverter import ImageInverter 
import numpy
from mock import Mock

class testImageInverter(unittest.TestCase):
    def testInverter(self):
        imageBlack = numpy.zeros((10,10,3))
        imageWhite = numpy.ones((10,10,3)) * 255
        
        target = ImageInverter()

        numpy.testing.assert_array_equal(imageBlack, target(imageWhite))
        numpy.testing.assert_array_equal(imageWhite, target(imageBlack))


if __name__=='__main__':
    unittest.main()
