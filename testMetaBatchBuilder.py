import unittest
from mock import Mock
from MetaBatchBuilder import MetaBatchBuilder
import numpy
from TestUtils import arrayEqualsTo

class testMetaBatchBuilder(unittest.TestCase):
    def setUp(self):
        self.target = MetaBatchBuilder()
        self.data_shape = (4,1,1)
    
    def test_dataMeanDoesNotConsiderTestSet(self):
        
        train = [self.makeImage([10, 20, 40, 80]),
                   self.makeImage([20, 40, 40, 60])]
        valid = [self.makeImage([10, 20, 40, 80]),
                   self.makeImage([20, 40, 40, 60])]
        test = [self.makeImage([1000, 2000, 4000, 8000]),
                   self.makeImage([2000, 4000, 4000, 6000])]
        
        dataset = (train, valid, test)
        classesNames = ['myname']
        classes = [0]
        
        expected = {}
        expected['num_vis'] = 4
        expected['data_shape'] = self.data_shape
        expected['data_in_rows']  = True
        expected['label_names'] = classesNames
        expected['data_mean'] = arrayEqualsTo(numpy.asarray([15, 30, 40, 70]).reshape(-1,1))

        self.assertEqual(expected, self.target.build(dataset, classes, classesNames))

    def test_OnlySelectedClassesAreStored(self):
        
        train = self.makeZeroedImages(qty=2, size=4)
        valid = self.makeZeroedImages(qty=2, size=4)
        test = self.makeZeroedImages(qty=2, size=4)
        
        dataset = (train, valid, test)
        classesNames = ['class0', 'class1', 'class2', 'class3']
        classes = [2,1]
        
        expected = {}
        expected['num_vis'] = 4
        expected['data_in_rows']  = True
        expected['data_shape'] = self.data_shape
        expected['label_names'] = ['class2', 'class1']
        expected['data_mean'] = arrayEqualsTo(numpy.zeros(4).reshape(-1,1))

        self.assertEqual(expected, self.target.build(dataset, classes, classesNames))

    def makeZeroedImages(self, qty, size):
        return [self.makeImage(numpy.zeros((size))) for i in range(qty)]

    def makeImage(self, array):
        image = Mock()
        image.getArray.return_value = numpy.asarray(array)
        image.getShape.return_value = self.data_shape
        return image

if __name__ == '__main__':
    unittest.main()
