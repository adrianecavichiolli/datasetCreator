from ConvnetDataset import *
import numpy as np
import cPickle

def selectRandomXclasses(X, total):
    selected = np.arange(total)
    np.random.shuffle(selected)
    return sorted(selected[:X])

def createDatasetBFL_115classes():
    sourceFolder = '/home/especial/vri/databases/autoria/BFL'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/BFL_115classes'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(315)
    classNumbers = selectRandomXclasses(115, 315)
    print("Using only 115 classes: %s\n", classNumbers)

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = FileGroupingSplit(numFilePerImage = 9),
                                            Grayscale = True,
                                            InvertColor = True)

def createDatasetIAM_240classes():
    sourceFolder = '/home/especial/vri/databases/autoria/IAM'
    classesFile = '/home/especial/vri/databases/autoria/IAMselected_240.pickle'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/IAM_240classes'
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
                                            InvertColor = True)

if __name__ == '__main__':
    createDatasetIAM_240classes()
    #createDatasetBFL_115classes()
