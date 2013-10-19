
class BatchBuilder:
    def __init__(self, singleBatchBuilder, metaBatchBuilder):
        self.singleBatchBuilder = singleBatchBuilder
        self.metaBatchBuilder = metaBatchBuilder
    
    def build(self, listOfImages, classes, classNames, datasetSplitIn):
        result = {}
        result['data_batch_1'] = self.singleBatchBuilder.build(listOfImages, classes)
        result['batches.meta'] = self.metaBatchBuilder.build(listOfImages, classNames)
        
        return result