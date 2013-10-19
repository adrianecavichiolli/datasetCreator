import unittest
from mock import  Mock, MagicMock, call
from BatchRepository import BatchRepository  

class testBatchRepository(unittest.TestCase):
    def testSave(self):
        filesystem = Mock()
        serializer = Mock()
        target = BatchRepository(filesystem, serializer)
        
        filesystem.joinPath = MagicMock(side_effect = lambda x,y: x + '/' + y)

        file1 = Mock()
        file2 = Mock()
        meta = Mock()
        batches = {'batches_1' : file1, 'data_batches_2' : file2, 'batches.meta': meta}
        target.save(batches, 'saveFolder')
        
        serializer.write.assert_has_calls([call('saveFolder/batches_1',file1),
                                          call('saveFolder/data_batches_2',file2),
                                          call('saveFolder/batches.meta',meta)], any_order=True) 