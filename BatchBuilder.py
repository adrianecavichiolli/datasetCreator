
class BatchBuilder:
    def __init__(self, singleBatchBuilder, metaBatchBuilder):
        self.singleBatchBuilder = singleBatchBuilder
        self.metaBatchBuilder = metaBatchBuilder
    
    def build(self, dataset, classes, classNames):
        result = {}
        result['data_batch_1'] = self.singleBatchBuilder.build(dataset[0], classes)
        result['data_batch_2'] = self.singleBatchBuilder.build(dataset[1], classes)
        result['data_batch_3'] = self.singleBatchBuilder.build(dataset[2], classes)
        result['batches.meta'] = self.metaBatchBuilder.build(dataset, classNames)
        
        return result