
class BatchBuilder:
    def __init__(self, singleBatchBuilder, metaBatchBuilder, nTrainingBatches = 1):
        self.singleBatchBuilder = singleBatchBuilder
        self.metaBatchBuilder = metaBatchBuilder
        self.nTrainingBatches = nTrainingBatches
    
    def build(self, dataset, classes, classNames):
        result = {}
        train, valid, test = dataset
        examplesPerBatch = int(len(train) / self.nTrainingBatches)
        
        for i in range(self.nTrainingBatches - 1):
            batchData = train[i*examplesPerBatch:(i+1)*examplesPerBatch]
            result['data_batch_%d' % (i + 1)] = self.singleBatchBuilder.build(batchData, classes)
        
        lastTrainingBatchData = train[(self.nTrainingBatches - 1)*examplesPerBatch:]
        result['data_batch_%d' % self.nTrainingBatches] = self.singleBatchBuilder.build(lastTrainingBatchData, classes)
            
        result['data_batch_%d' % (self.nTrainingBatches + 1)] = self.singleBatchBuilder.build(valid, classes)
        result['data_batch_%d' % (self.nTrainingBatches + 2)] = self.singleBatchBuilder.build(test, classes)
        result['batches.meta'] = self.metaBatchBuilder.build(dataset, classes, classNames)
        
        return result