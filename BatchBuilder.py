import os

class BatchBuilder:
    def __init__(self, singleBatchBuilder):
        self.singleBatchBuilder = singleBatchBuilder
    
    def build(self, listOfImages, savePath):
        self.singleBatchBuilder.build(listOfImages, os.path.join(savePath, 'data_batch_1'))
        