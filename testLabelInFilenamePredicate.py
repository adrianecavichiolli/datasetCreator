import unittest
from LabelInFilenamePredicate import LabelInFilenamePredicate

class testLabelInFilenamePredicate(unittest.TestCase):
    def test_validFilenames(self):
        acceptedClasses = [0,1,2,4]
        target = LabelInFilenamePredicate(acceptedClasses)
        
        self.assertTrue(target('0101.jpg'))
        self.assertTrue(target('0201.jpg'))
        self.assertTrue(target('0315.jpg'))
        self.assertFalse(target('0415.jpg'))
        self.assertTrue(target('0501.jpg'))
        self.assertFalse(target('0615.jpg'))
        self.assertFalse(target('00615.jpg'))
        self.assertFalse(target('something'))
