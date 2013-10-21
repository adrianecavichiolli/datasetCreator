import numpy

class ClassBalancingDatasetSplitter:
    def split(self, data, datasetSplitIn):
        train = []
        valid = []
        test = []
        
        classes = self.getDistinctClasses(data)
        for currentClass in classes:
            curTrain, curValid, curTest = self.splitForClass(data, datasetSplitIn, currentClass)
            train += curTrain
            valid += curValid
            test += curTest
        
        numpy.random.shuffle(train)
        numpy.random.shuffle(valid)
        numpy.random.shuffle(test)
        
        return (train,valid, test)

    def getDistinctClasses(self,data):
        labels = [item.getLabel() for item in data]
        return set(labels)    
    
    def splitForClass(self, data, datasetSplitIn, currentClass):
        classData = self.getClassData(data, currentClass)
        
        firstValidationIndex = datasetSplitIn[0] * len(classData)
        firstTestIndex = firstValidationIndex + datasetSplitIn[1] * len(classData)
        
        numpy.random.shuffle(classData)
        result = numpy.split(classData, [firstValidationIndex, firstTestIndex])
        return (item.tolist() for item in result)
         
    def getClassData(self, data, currentClass):
        return [item for item in data if item.getLabel() == currentClass]
        
        