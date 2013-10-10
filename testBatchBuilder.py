import unittest
from mock import Mock
from BatchBuilder import BatchBuilder

class testBatchBuilder:
    def test(self):
        singleBatchBuilder = Mock()
        listOfImages = Mock()
        pathToSave = Mock()

        target = BatchBuilder(singleBatchBuilder)
        
        target.build(listOfImages, pathToSave)