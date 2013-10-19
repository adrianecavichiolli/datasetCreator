import unittest
from DatasetSplitter import DatasetSplitter
import numpy

class testDatasetSplitter(unittest.TestCase):
    def setUp(self):
        self.target = DatasetSplitter()
        
    def testSplitUnionIsEqualToTotal(self):
        items = range(15)
        result = self.target.split(items, [.6,.2,.2])
        
        aggregated_result = numpy.concatenate(result).tolist()
        self.assertEqual(sorted(aggregated_result), sorted(items))
        
    def testSplitIntersectionIsEmpy(self):
        items = range(15)
        result = self.target.split(items, [.6,.2,.2])
        self.assertEqual(0, len(numpy.intersect1d(result[0], result[1])))
        self.assertEqual(0, len(numpy.intersect1d(result[1], result[2])))
        self.assertEqual(0, len(numpy.intersect1d(result[0], result[2])))