import unittest
from PredicateDatasetSplitter import PredicateDatasetSplitter
import numpy
from mock import Mock

class testPredicateDatasetSplitter(unittest.TestCase):
    
    def test_noFilenameMatches_ReturnDatasetWithTrainOnly(self):
        items = ["001_%d.png" % (i) for i in range(15)]
        alwaysFalse = lambda x:False
        target = PredicateDatasetSplitter(alwaysFalse, alwaysFalse)
        result = target.split(items)
        
        self.assertEqual(items, result[0])
        self.assertEqual(0, len(result[1]))
        self.assertEqual(0, len(result[2]))
    
    def test_filenameMatches_ReturnImagesPartitionedInTrainValidTest(self):
        items = ["001_%d" % (i) for i in range(15)]
        
        isInValidation = createMatcherWithTrueFor(["001_2","001_4","001_9"])
        
        isInTest = createMatcherWithTrueFor(["001_3","001_5"])
        
        target = PredicateDatasetSplitter(isInValidation, isInTest)
        train, valid, test = target.split(items)
        
        self.assertEqual(10, len(train))
        self.assertEqual(["001_2","001_4","001_9"], sorted(valid))
        self.assertEqual(["001_3","001_5"], sorted(test))
        

def createMatcherWithTrueFor(elements):
    return lambda x: x in elements

if __name__=='__main__':
    unittest.main()
