
from ConvnetDataset import *


def createDatasetGenre_point6():
    sourceFolder = '/home/especial/vri/databases/generos_musicais/classinname'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/Genre_resized'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(10)
    classNumbers = range(10)

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent(0.6),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True)
        

if __name__ == '__main__':
    createDatasetGenre_point6()

