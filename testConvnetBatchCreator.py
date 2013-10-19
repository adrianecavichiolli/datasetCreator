import unittest
from ConvnetBatchCreator import ConvnetBatchCreator
from mock import Mock

class testConvnetBatchCreator(unittest.TestCase):
    def testBuildAndSaveBatches(self):
        batchBuilder = Mock()
        batchRepository = Mock()
        target = ConvnetBatchCreator(batchBuilder = batchBuilder, batchRepository = batchRepository)
        
        dataset = Mock()
        batches = Mock()
        classes = [1]
        classNames = ['myclass1']
        saveFolder = 'saveFolder'
        
        target.batchBuilder.build.return_value = batches
        
        target.buildBatches(dataset, classes, classNames, saveFolder)
        
        batchBuilder.build.assert_called_with(dataset, classes, classNames)
        batchRepository.save.assert_called_with(batches, saveFolder)