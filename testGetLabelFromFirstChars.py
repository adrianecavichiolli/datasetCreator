import unittest
from GetLabelFromFirstChars import GetLabelFromFirstChars
from TestUtils import *

class testLabeledImage(unittest.TestCase):
    def test_extractlabelsFromFIrstTwo(self):
        getlabelFromFirstTwo = GetLabelFromFirstChars(nChars=2)
        self.assertEqual(0, getlabelFromFirstTwo('0101.jpg'))
        self.assertEqual(1, getlabelFromFirstTwo('0222.jpg'))
        self.assertEqual(5, getlabelFromFirstTwo('0651.jpg'))
        self.assertEqual(42, getlabelFromFirstTwo('4330.jpg'))

    def test_extractlabelsFromFirstThree(self):
        getlabelFromFirstThree = GetLabelFromFirstChars(nChars=3)
        self.assertEqual(0, getlabelFromFirstThree('00101.jpg'))
        self.assertEqual(1, getlabelFromFirstThree('00222.jpg'))
        self.assertEqual(5, getlabelFromFirstThree('00651.jpg'))
        self.assertEqual(42, getlabelFromFirstThree('04330.jpg'))
        self.assertEqual(104, getlabelFromFirstThree('10530.jpg'))
        
        
if __name__ == '__main__':
    unittest.main()
