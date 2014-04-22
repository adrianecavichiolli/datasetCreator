import unittest
from PercentageImageResizer import PercentageImageResizer
from mock import Mock
from TestUtils import *

class testPercentageImageResizer(unittest.TestCase):
    def setUp(self):
        self.imageResizer = Mock()
        
    def test_Percentage1_ReturnSameImage(self):
        source = numpy.zeros((2,2,3))
        source[:,:,0] =  [[0,1], [2,3]]
        source[:,:,1] =  [[4,5], [6,7]]
        source[:,:,2] =  [[8,9], [10,11]]
        
        target = PercentageImageResizer(self.imageResizer, 1)
        target(source)

        numpy.testing.assert_array_equal(source, target(source))
        
    def test_Percentage_point5_ReturnHalfImage(self):
        source = numpy.zeros((50,30,3))
        
        self.imageResizer.resize.return_value = resized = Mock()
        
        target = PercentageImageResizer(self.imageResizer, 0.5)
        target(source)

        self.imageResizer.resize.assert_called_with(arrayEqualsTo(source), (25,15))
        
    def test_Percentage_point5_ReturnHalfImage_ensureIntegerSize(self):
        source = numpy.zeros((21,51,3))
        
        self.imageResizer.resize.return_value = resized = Mock()
        
        target = PercentageImageResizer(self.imageResizer, 0.5)
        target(source)

        self.imageResizer.resize.assert_called_with(arrayEqualsTo(source), (10,25))
