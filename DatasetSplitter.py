import numpy
class DatasetSplitter:
    def split(self, data, datasetSplitIn):
        totalItems = len(data)
        indices = numpy.arange(totalItems)
        numpy.random.shuffle(indices)
        
        trainCount = int(datasetSplitIn[0] * totalItems)
        validCount = int(datasetSplitIn[1] * totalItems)
        
        train = [data[indices[i]] for i in range(trainCount)]
        valid = [data[indices[i]] for i in range(trainCount, trainCount + validCount)]
        test =  [data[indices[i]] for i in range(trainCount + validCount, totalItems)]
        
         
        return (train,valid, test)