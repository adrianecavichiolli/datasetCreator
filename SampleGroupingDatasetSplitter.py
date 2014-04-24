import re
import numpy
from itertools import groupby

class SampleGroupingDatasetSplitter:
    def __init__(self, getSampleNumberFunction):
        self.getSampleNumber = getSampleNumberFunction

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

    def splitForClass(self, data, datasetSplitIn, currentClass):
        classData = self.getClassData(data, currentClass)
        
        sortedData = sorted(classData, key = self.getSampleNumber)
        groups = []
        for k, group in groupby(sortedData, self.getSampleNumber):
            groups.append(list(group))
        
        numpy.random.shuffle(groups)
        
        firstValidationIndex = datasetSplitIn[0] * len(groups)
        firstTestIndex = firstValidationIndex + datasetSplitIn[1] * len(groups)
        
        splitGroups = numpy.split(groups, [firstValidationIndex, firstTestIndex])
        
        return (self.flattenList(g) for g in splitGroups)

    def flattenList(self, listOfLists):
        return [item for sublist in listOfLists for item in sublist]
        
    def getDistinctClasses(self,data):
        labels = [item.getLabel() for item in data]
        return set(labels)    

    def getClassData(self, data, currentClass):
        return numpy.asarray([item for item in data if item.getLabel() == currentClass])

