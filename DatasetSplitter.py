import numpy

class DatasetSplitter:
    def split(self, data, datasetSplitIn):
        firstValidationIndex = datasetSplitIn[0] * len(data)
        firstTestIndex = firstValidationIndex + datasetSplitIn[1] * len(data)
        
        numpy.random.shuffle(data)
        result = numpy.split(data, [firstValidationIndex, firstTestIndex])
        return tuple(item.tolist() for item in result)
