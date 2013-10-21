import unittest
from ClassBalancingDatasetSplitter import ClassBalancingDatasetSplitter
import numpy
from mock import Mock

class testClassBalancingDatasetSplitter(unittest.TestCase):
    def setUp(self):
        self.target = ClassBalancingDatasetSplitter()
        
    def testSplitUnionIsEqualToTotal(self):
        items = self.createImages(15, label = 0)
        result = self.target.split(items, [.6,.2,.2])
             
        aggregated_result = result[0] + result[1] + result[2]

        self.assertEqual(sorted(aggregated_result), sorted(items))
        
    def testSplitIntersectionIsEmpy(self):
        items = self.createImages(15, label = 0)
        result = self.target.split(items, [.6,.2,.2])
        self.assertEqual(0, len(numpy.intersect1d(result[0], result[1])))
        self.assertEqual(0, len(numpy.intersect1d(result[1], result[2])))
        self.assertEqual(0, len(numpy.intersect1d(result[0], result[2])))
        
    def testClassAreBalanced(self):
        items0 = self.createImages(10, label = 0)
        items1 = self.createImages(5, label = 1)
        items2 = self.createImages(100, label = 2)
        items3 = self.createImages(200, label = 3)
        items = items0 + items1 + items2 + items3
        
        result = self.target.split(items, [.6, .2, .2])

        self.assertNumberOfItemsInResultWithLabel([6, 2, 2], result, label = 0)
        self.assertNumberOfItemsInResultWithLabel([3, 1, 1], result, label = 1)
        self.assertNumberOfItemsInResultWithLabel([60, 20, 20], result, label = 2)
        self.assertNumberOfItemsInResultWithLabel([120, 40, 40], result, label = 3)

    def assertNumberOfItemsInResultWithLabel(self, n, result, label):
        for i in range(3):
            self.assertEquals(n[i], self.NumberOfItemsWithLabel(result[i], label))
    
    def NumberOfItemsWithLabel(self, array, label):
        return sum(1 if item.getLabel() == label else 0 for item in array)
    
    def createImage(self, label):
        image = Mock()
        image.getLabel.return_value = label
        return image
    
    def createImages(self, quantity, label):
        return [self.createImage(label) for i in range(quantity)]