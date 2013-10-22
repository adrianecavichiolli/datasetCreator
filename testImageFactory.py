import unittest
from  LabeledImage import LabeledImage
from TestUtils import *

class testLabeledImage(unittest.TestCase):
    def test_extractlabels(self):
        self.assertEqual(0, LabeledImage.getLabelFromFilename('0101.jpg'))
        self.assertEqual(1, LabeledImage.getLabelFromFilename('0222.jpg'))
        self.assertEqual(5, LabeledImage.getLabelFromFilename('0651.jpg'))
        self.assertEqual(42, LabeledImage.getLabelFromFilename('4330.jpg'))
    
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
