import unittest
from mock import Mock, MagicMock
from BatchBuilder import BatchBuilder

class testBatchBuilder(unittest.TestCase):
    def test(self):
        singleBatchBuilder = Mock()
        listOfImages = Mock()
        pathToSave = 'data'
        metaBatchBuilder = Mock()
        fileSystem = Mock()
        classes = [0]
        classNames = ['class']

        fileSystem.joinPath = MagicMock(side_effect = lambda x,y: x + '/' + y)

        target = BatchBuilder(singleBatchBuilder, metaBatchBuilder, fileSystem)
        
        target.build(listOfImages, classes, classNames, pathToSave)

        singleBatchBuilder.build.assert_called_with(listOfImages, classes, 'data/data_batch_1')
        metaBatchBuilder.build.assert_called_with(listOfImages, classNames, 'data/batches.meta')
        
if __name__ == '__main__':
    unittest.main()
