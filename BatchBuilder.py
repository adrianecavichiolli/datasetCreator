
class BatchBuilder:
    def __init__(self, singleBatchBuilder, metaBatchBuilder, fileSystem):
        self.singleBatchBuilder = singleBatchBuilder
        self.metaBatchBuilder = metaBatchBuilder
        self.fileSystem = fileSystem
    
    def build(self, listOfImages, classes, classNames, savePath):
        self.singleBatchBuilder.build(listOfImages, classes, self.fileSystem.joinPath(savePath, 'data_batch_1'))
        self.metaBatchBuilder.build(listOfImages, classNames, self.fileSystem.joinPath(savePath, 'batches.meta'))