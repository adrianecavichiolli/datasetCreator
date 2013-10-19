import unittest
from mock import Mock
from BatchBuilder import BatchBuilder

class testBatchBuilder(unittest.TestCase):
    def setUp(self):
        self.singleBatchBuilder = Mock()
        self.metaBatchBuilder = Mock()
        self.target = BatchBuilder(self.singleBatchBuilder, self.metaBatchBuilder)
        
    def test(self):
        batch1 = Mock()
        batch2 = Mock()
        batch3 = Mock()
        meta = Mock()
        self.singleBatchBuilder.build.side_effect = [batch1, batch2, batch3]
        self.metaBatchBuilder.build.return_value = meta

        listOfImages = Mock()

        classes = [0]
        classNames = ['class']
      
        result = self.target.build(listOfImages, classes, classNames, Mock())

        self.singleBatchBuilder.build.call_args_list
        
        
        self.metaBatchBuilder.build.assert_called_with(listOfImages, classNames)
        
        self.assertEqual({'data_batch_1' : batch1,
                          'data_batch_2' : batch2,
                          'data_batch_3' : batch3,
                          'batches.meta' : meta}, result)
        
        
if __name__ == '__main__':
    unittest.main()
