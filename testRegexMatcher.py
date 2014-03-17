import unittest
from FileNumberRegexMatcher import FileNumberRegexMatcher 
import numpy
from mock import Mock

class testFileNumberRegexMatcher(unittest.TestCase):
    def test_NumberInList_returnTrue(self):
        target = FileNumberRegexMatcher(range(1,10))
        self.assertTrue(target(image('034_1.bmp')))
        self.assertTrue(target(image('315_3.bmp')))
        self.assertTrue(target(image('001_2.bmp')))
        self.assertTrue(target(image('001_9.bmp')))

    def test_NumberNotInList_returnFalse(self):
        target = FileNumberRegexMatcher(range(1,10))
        self.assertFalse(target(image('034_10.bmp')))
        self.assertFalse(target(image('315_25.bmp')))
        self.assertFalse(target(image('001_27.bmp')))

def image(filename):
    img = Mock()
    img.getFilename.return_value=filename
    return img

if __name__=='__main__':
    unittest.main()
