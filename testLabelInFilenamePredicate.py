import unittest
from LabelInFilenamePredicate import LabelInFilenamePredicate
from GetLabelFromFirstChars import GetLabelFromFirstChars

class testLabelInFilenamePredicate(unittest.TestCase):
    def test_validFilenames(self):
        acceptedClasses = [0,1,2,4]
        target = LabelInFilenamePredicate(GetLabelFromFirstChars(2), acceptedClasses)
        
        self.assertTrue(target('0101.jpg'))
        self.assertTrue(target('0201.jpg'))
        self.assertTrue(target('0315.jpg'))
        self.assertFalse(target('0415.jpg'))
        self.assertTrue(target('0501.jpg'))
        self.assertFalse(target('0615.jpg'))
        self.assertFalse(target('00615.jpg'))
        self.assertFalse(target('something'))

    def test_validFilenames3chars(self):
        acceptedClasses = [0,1,2,4]
        target = LabelInFilenamePredicate(GetLabelFromFirstChars(3), acceptedClasses)
        
        self.assertTrue(target('00101.jpg'))
        self.assertTrue(target('00201.jpg'))
        self.assertTrue(target('00315.jpg'))
        self.assertFalse(target('00415.jpg'))
        self.assertTrue(target('00501.jpg'))
        self.assertFalse(target('00615.jpg'))
        self.assertFalse(target('615.jpg'))
        self.assertFalse(target('something'))
