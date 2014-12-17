from ConvnetDataset import *



def createDatasetKylberg():
    sourceFolder = '/home/especial/vri/databases/texturas/KylbergTextureDataset-1.0-png-originals'
    saveFolder = '/home/especial/vri/databases/preprocessados/kylberg'
    expectedDistribution = [0.5, 0.3, 0.2]

    classNames = range(27)
    classNumbers = range(27)

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True,
                                            NumTrainBatches = 1)

if __name__ == '__main__':
    createDatasetKylberg()

