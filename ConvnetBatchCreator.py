class ConvnetBatchCreator:
    def __init__(self, batchBuilder, batchRepository):
        self.batchBuilder = batchBuilder
        self.batchRepository = batchRepository 
    def buildBatches(self, dataset, classes, classNames, saveFolder):
        batches = self.batchBuilder.build(dataset, classes, classNames)
        self.batchRepository.save(batches, saveFolder)