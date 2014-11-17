import unittest
from FixedDatasetSplitter import FixedDatasetSplitter
import numpy
from mock import Mock

class testFixedDatasetSplitter(unittest.TestCase):

    def testSplitUnionIsEqualToTotal(self):
        items = [imageNamed(0,"001_01.bmp"), imageNamed(0,"001_03.bmp"), imageNamed(0,"001_02.bmp")]
        target = FixedDatasetSplitter(filenames_in_train=["001_02.bmp"],
                                      filenames_in_valid=["001_03.bmp"],
                                      filenames_in_test=["001_01.bmp"])
        result = target.split(items, [.6,.2,.2])

        aggregated_result = result[0] + result[1] + result[2]

        self.assertEqual(sorted(aggregated_result), sorted(items))

    def testSplitIntersectionIsEmpy(self):
        items = [imageNamed(0,"001_01.bmp"), imageNamed(0,"001_03.bmp"), imageNamed(0,"001_02.bmp")]
        target = FixedDatasetSplitter(filenames_in_train=["001_02.bmp"],
                                      filenames_in_valid=["001_03.bmp"],
                                      filenames_in_test=["001_01.bmp"])
        result = target.split(items, [.6,.2,.2])
        self.assertEqual(0, len(numpy.intersect1d(result[0], result[1])))
        self.assertEqual(0, len(numpy.intersect1d(result[1], result[2])))
        self.assertEqual(0, len(numpy.intersect1d(result[0], result[2])))

    def testOrderIsPreservedInSplit(self):
        items = [imageNamed(0,"001_01.bmp"), imageNamed(0,"001_02.bmp"), imageNamed(0,"001_03.bmp"),
                 imageNamed(0,"001_04.bmp"), imageNamed(0,"001_05.bmp"), imageNamed(0,"001_06.bmp")]

        target = FixedDatasetSplitter(filenames_in_train=["001_06.bmp", "001_01.bmp"],
                                      filenames_in_valid=["001_05.bmp", "001_04.bmp"],
                                      filenames_in_test=["001_03.bmp", "001_02.bmp"])

        train, valid, test = target.split(items, [.6,.2,.2])

        self.assertEqual("001_06.bmp", train[0].getFilename())
        self.assertEqual("001_01.bmp", train[1].getFilename())
        self.assertEqual("001_05.bmp", valid[0].getFilename())
        self.assertEqual("001_04.bmp", valid[1].getFilename())
        self.assertEqual("001_03.bmp", test[0].getFilename())
        self.assertEqual("001_02.bmp", test[1].getFilename())

    def testThrowsErrorIfItemNotFound(self):
        items = [imageNamed(0,"001_01.bmp"), imageNamed(0,"001_02.bmp"), imageNamed(0,"001_03.bmp")]
        target = FixedDatasetSplitter(filenames_in_train=["does_not_exist"],
                                      filenames_in_valid=["001_03.bmp"],
                                      filenames_in_test=["001_01.bmp"])

        self.assertRaises(Exception, target.split, items, [.6,.2,.2])

    def createImage(self, label):
        image = Mock()
        image.getLabel.return_value = label
        return image

    def createImages(self, quantity, label):
        return [self.createImage(label) for i in range(quantity)]


def imageNamed(label, name):
    img = Mock()
    img.getLabel.return_value=label
    img.getFilename.return_value = name
    img.__str__ = Mock(return_value = name)
    return img
