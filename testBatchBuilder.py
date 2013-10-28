import unittest
from mock import Mock, call
from BatchBuilder import BatchBuilder

class testBatchBuilder(unittest.TestCase):
    def setUp(self):
        self.singleBatchBuilder = Mock()
        self.metaBatchBuilder = Mock()
        
    def testSingleTrainingBatch(self):
        batch1, batch2, batch3, meta = (Mock(), Mock(), Mock(), Mock())
        self.singleBatchBuilder.build.side_effect = [batch1, batch2, batch3]
        self.metaBatchBuilder.build.return_value = meta

        train, valid, test = ([Mock()], Mock(), Mock())
        dataset = (train, valid, test)

        classes = [0]
        classNames = ['class']

        self.target = BatchBuilder(self.singleBatchBuilder, 
                                   self.metaBatchBuilder, 
                                   nTrainingBatches = 1)
        result = self.target.build(dataset, classes, classNames)

        self.singleBatchBuilder.build.assert_has_calls([call(train, classes), 
                                                        call(valid,classes),
                                                        call(test,classes)])
               
        self.metaBatchBuilder.build.assert_called_with(dataset, classes, classNames)
        
        self.assertEqual({'data_batch_1' : batch1,
                          'data_batch_2' : batch2,
                          'data_batch_3' : batch3,
                          'batches.meta' : meta}, result)
                          
    def testMultipleTrainingBatches(self):       
        self.singleBatchBuilder.build.side_effect = batches = [Mock() for i in range(5)] 
        self.metaBatchBuilder.build.return_value = meta = Mock()
        
        train = [Mock() for i in range(11)]
        valid, test = (Mock(), Mock())
        dataset = (train, valid, test)

        classes = [0]
        classNames = ['class']

        self.target = BatchBuilder(self.singleBatchBuilder, 
                                   self.metaBatchBuilder, 
                                   nTrainingBatches = 3)
        result = self.target.build(dataset, classes, classNames)

        self.singleBatchBuilder.build.assert_has_calls([call(train[:3], classes),
                                                        call(train[3:6], classes),
                                                        call(train[6:], classes), 
                                                        call(valid,classes),
                                                        call(test,classes)])
               
        self.metaBatchBuilder.build.assert_called_with(dataset, classes, classNames)
        
        self.assertEqual({'data_batch_1' : batches[0],
                          'data_batch_2' : batches[1],
                          'data_batch_3' : batches[2],
                          'data_batch_4' : batches[3],
                          'data_batch_5' : batches[4],
                          'batches.meta' : meta}, result)
        
if __name__ == '__main__':
    unittest.main()
