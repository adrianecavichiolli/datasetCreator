from ConvnetDataset import *
import numpy as np
import cPickle

def selectRandomXclasses(X, total):
    selected = np.arange(total)
    np.random.shuffle(selected)
    return sorted(selected[:X])

def createDatasetBFL_115classes(fold):
    sourceFolder = '/home/especial/vri/databases/autoria/BFL'
    classesFile = '/home/especial/vri/databases/autoria/BFLselected_115.pickle'
    saveFolder  = '/home/especial/vri/databases/preprocessados/BFL_115_1trainbatch_%d' % fold
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(315)
    selectedClasses = cPickle.load(open(classesFile))
    classNumbers = selectedClasses

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = FileGroupingSplit(numFilePerImage = 9),
                                            Grayscale = True,
                                            InvertColor = True,
                                            NumTrainBatches = 1)

def createDatasetIAM_240classes(fold):
    sourceFolder = '/home/especial/vri/databases/autoria/IAM'
    classesFile = '/home/especial/vri/databases/autoria/IAMselected_240.pickle'
    saveFolder  = '/home/especial/vri/databases/preprocessados/IAM_240_1trainbatch_%d' % fold
    expectedDistribution = [0.5, 0, 0.5]

    selectedClasses = cPickle.load(open(classesFile))

    classNames = range(672)
    classNumbers = selectedClasses

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            SplitFunction = GroupingSplit(),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True,
                                            InvertColor = True,
                                            NumTrainBatches = 2)

if __name__ == '__main__':
    #createDatasetIAM_240classes(2)
    #createDatasetIAM_240classes(3)
    createDatasetBFL_115classes(2)
    createDatasetBFL_115classes(3)
