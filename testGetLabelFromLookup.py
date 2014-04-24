import unittest
from mock import Mock, call
from GetLabelFromLookup import *

class testGetLabelFromLookup(unittest.TestCase):
    def setUp(self):
        self.someClasses = ["some","another"]

    def testGetLabel_ReturnsNumberInLookupTable(self):
        classNames = ["zero", "one", "two", "three", "someOther"]

        target = GetLabelFromLookup(classNames= classNames, separator= "_")

        self.assertEqual(0, target("zero_01.png"))
        self.assertEqual(1, target("one_01.png"))
        self.assertEqual(2, target("two_23.png"))
        self.assertEqual(3, target("three_2323.png"))
        self.assertEqual(4, target("someOther_2322.png"))

    def testThrowsIfSeparatorNotFound(self):
        target = GetLabelFromLookup(classNames = self.someClasses, separator = "_")
        self.assertRaises(FilenameDoesNotContainSeparatorError, target, "noseparator.png")

    def testThrowsIfClassNotFound(self):
        target = GetLabelFromLookup(classNames = ["first", "second"], separator = "_")
        self.assertRaises(FilenameContainsClassNotInLookup, target, "invalidclass_01.png")


if __name__ == '__main__':
    unittest.main()
