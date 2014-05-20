
from ConvnetDataset import *
from DatasetGridExtractor import DatasetGridExtractor

def createDatasetGenre_point6():
    sourceFolder = '/home/especial/vri/databases/generos_musicais/classinname'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/Genre_first_part'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(10)
    classNumbers = range(10)

    dataset = ConvnetDataset.CreateDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent(0.6),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True)

    gridExtractor = DatasetGridExtractor()
    datasets = gridExtractor.run(numRows = 10, numCols = 3)


    mydata = (datasets[0][0], datasets[1][0], datasets[2][0])
    convnetBatchCreator.buildBatches(dataset = mydata, 
                                     classes = classNumbers,
                                     classNames = classNames,
                                     saveFolder = saveFolder)
        

if __name__ == '__main__':
    createDatasetGenre_point6()

