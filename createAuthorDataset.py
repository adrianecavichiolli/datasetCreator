from ConvnetDataset import *

def createDatasetBFL_256_inv():
    sourceFolder = '/home/especial/vri/databases/autoria/BFL'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/BFL_64_inv_split'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(315)
    classNumbers = range(315)

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = FileGroupingSplit(numFilePerImage = 9),
                                            Grayscale = True,
                                            InvertColor = True)

def createDatasetIAM():
    sourceFolder = '/home/especial/vri/databases/autoria/IAM'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/IAM_orig'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(672)
    classNumbers = range(672)

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True,
                                            InvertColor = True)

if __name__ == '__main__':
    createDatasetBFL_256_inv()
    #createDatasetIAM()
