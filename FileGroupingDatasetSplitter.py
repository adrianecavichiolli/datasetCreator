import re
import numpy

class FileGroupingDatasetSplitter:
    def __init__(self, numFilesPerImage, shuffle=True):
        self.numFilesPerImage = numFilesPerImage
        self.regex = re.compile(".*_(.*)\.")
        self.shuffle = shuffle

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
        
        filenames = [img.getFilename() for img in classData]
        fileNum = [int(self.regex.match(f).group(1)) for f in filenames]
        assert len(fileNum) % self.numFilesPerImage == 0, "Number of samples for a class must divide numFilesPerImage. Samples: %d, numFilesPerImage: %d" % (len(fileNum), self.numFilesPerImage)
        assert sorted(fileNum) == range(1, len(fileNum)+1), "Samples should be a sequence from 1 to %d. %s" %(len(fileNum), fileNum)

        numGroups = len(fileNum) / self.numFilesPerImage
        groupedFilenames = []
        for i in range(numGroups):
            seqForThisGroup = range(1 + i * self.numFilesPerImage, 1 + (i+1)* self.numFilesPerImage)
            wanted =  numpy.where([f in seqForThisGroup for f in fileNum])
            groupedFilenames.append(classData[wanted])
        

        if (self.shuffle):
            numpy.random.shuffle(groupedFilenames)
        return (item.tolist() for item in groupedFilenames)
         
    def getClassData(self, data, currentClass):
        return numpy.asarray([item for item in data if item.getLabel() == currentClass])
        
        
