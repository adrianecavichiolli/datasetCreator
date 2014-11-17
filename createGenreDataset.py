
from ConvnetDataset import *
from DatasetGridExtractor import DatasetGridExtractor

def createDatasetGenre_folds():
    sourceFolder = '/home/especial/vri/databases/generos_musicais/classinname'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/genreparts_folds/'
    expectedDistribution = [0.3, 0.3, 0.4]

    classNames = range(10)
    classNumbers = range(10)

    dataset = ConvnetDataset.CreateDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent(0.6),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = FileGroupingSplit(30, False),
                                            Grayscale = True)

    gridExtractor = DatasetGridExtractor(numRows = 10, numCols = 3)
    datasets = gridExtractor.run(dataset)

    for i in xrange(30):
        mydata = (datasets[0][i], datasets[1][i], datasets[2][i])

        convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 1)
        convnetBatchCreator.buildBatches(dataset = mydata, 
                                     classes = classNumbers,
                                     classNames = classNames,
                                     saveFolder = saveFolder + str(i))

def createDatasetGenre_noresize_folds():
    sourceFolder = '/home/especial/vri/databases/generos_musicais/classinname'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/genreparts_noresize_folds/'
    expectedDistribution = [0.3, 0.3, 0.4]

    classNames = range(10)
    classNumbers = range(10)

    dataset = ConvnetDataset.CreateDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = FileGroupingSplit(30, False),
                                            Grayscale = True)

    gridExtractor = DatasetGridExtractor(numRows = 10, numCols = 3)
    datasets = gridExtractor.run(dataset)

    for i in xrange(30):
        mydata = (datasets[0][i], datasets[1][i], datasets[2][i])

        convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 1)
        convnetBatchCreator.buildBatches(dataset = mydata, 
                                     classes = classNumbers,
                                     classNames = classNames,
                                     saveFolder = saveFolder + str(i))

if __name__ == '__main__':
    createDatasetGenre_noresize_folds()

