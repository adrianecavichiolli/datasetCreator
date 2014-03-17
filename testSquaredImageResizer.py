import unittest
from SquaredImageResizer import SquaredImageResizer
from mock import Mock
from TestUtils import *

class testSquaredImageResizer(unittest.TestCase):
    def setUp(self):
        self.imageResizer = Mock()
        
    def test_squaredImageWithFinalSize_ReturnSameImage(self):
        source = numpy.zeros((2,2,3))
        source[:,:,0] =  [[0,1], [2,3]]
        source[:,:,1] =  [[4,5], [6,7]]
        source[:,:,2] =  [[8,9], [10,11]]
        
        target = SquaredImageResizer(self.imageResizer, 2)
        target(source)

        numpy.testing.assert_array_equal(source, target(source))
        
    def test_squaredImage_CallResizeWithImage(self):
        source = numpy.zeros((10,10,3))

        self.imageResizer.resize.return_value = resized = Mock()

        target = SquaredImageResizer(self.imageResizer, 5)
        result = target(source)
        
        self.assertEquals(result, resized)
        self.imageResizer.resize.assert_called_with(arrayEqualsTo(source), (5,5))
    
    def test_imageWithLargerWidth_CallResizeWithCroppedImage(self):
        source = numpy.zeros((10,20,3))
        
        expected = numpy.ones((10,10,3))
        expected[:,:,1] *= 2
        expected[:,:,2] *= 3
        
        source[:,5:15,:] = expected
        
        target = SquaredImageResizer(self.imageResizer, 10)
        target(source)
        
        self.imageResizer.resize.assert_called_with(arrayEqualsTo(expected), (10,10))
        
    def test_imageWithLargerHeight_CallResizeWithCroppedImage(self):
        source = numpy.zeros((20,10,3))
        
        expected = numpy.ones((10,10,3))
        expected[:,:,1] *= 2
        expected[:,:,2] *= 3
        
        source[5:15,:,:] = expected
        
        target = SquaredImageResizer(self.imageResizer, 10)
        target(source)
        
        self.imageResizer.resize.assert_called_with(arrayEqualsTo(expected), (10,10))
    
    def test_grayScale_CallResizeWithCroppedImage(self):
        source = numpy.zeros((20,10))
        expected = numpy.ones((10,10))
        
        source[5:15,:] = expected
        
        target = SquaredImageResizer(self.imageResizer, 10)
        target(source)
        
        self.imageResizer.resize.assert_called_with(arrayEqualsTo(expected), (10,10))
