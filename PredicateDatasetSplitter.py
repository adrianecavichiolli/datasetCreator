import numpy

class PredicateDatasetSplitter:
    def __init__(self, shouldBeInValid, shouldBeInTest):
        self.shouldBeInValid = shouldBeInValid
        self.shouldBeInTest = shouldBeInTest

    def split(self, data, datasetSplitIn = None):
        train = []
        valid =[]
        test = []
        
        numpy.random.shuffle(data)
        for item in data:
            if self.shouldBeInValid(item):
                valid.append(item)
            elif self.shouldBeInTest(item):
                test.append(item)
            else:
                train.append(item)

        return (train, valid, test)
