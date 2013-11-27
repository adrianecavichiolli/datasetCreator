import unittest
from  LabeledImage import LabeledImage
from TestUtils import *

class testLabeledImage(unittest.TestCase):
    
    def test_getArrayOrdersDataCorrectly(self):
        original = numpy.zeros((2,2,3))
        original[:,:,0] =  [[0,1], [2,3]]
        original[:,:,1] =  [[4,5], [6,7]]
        original[:,:,2] =  [[8,9], [10,11]]
        
        target = LabeledImage(original, 0, 'file')
        
        expected = arrayEqualsTo(numpy.arange(12))
        
        self.assertEqual(expected, target.getArray())
        
if __name__ == '__main__':
    unittest.main()
