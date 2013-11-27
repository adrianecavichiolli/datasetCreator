from DatasetCreatorFactory import DatasetCreatorFactory
from ImageDataSourceFactory import ImageDataSourceFactory
from ConvnetBatchCreatorFactory import ConvnetBatchCreatorFactory
from PreprocessorFactory import PreprocessorFactory

sourceFolder = '/home/especial/vri/databases/florestais-macro'

def createDataset_halfToTest():
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/treesallclasses'
    expectedDistribution = [0.35, 0.15, 0.5]

    preprocessor = PreprocessorFactory.CreateExtractGridPatches(64)

    imageSource = ImageDataSourceFactory.CreateResizingImageSource(
                      sourceFolder = sourceFolder,
                      newSize = 256, log=True, 
                      loadOnlyClasses=range(41))

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource, 
                                                  preprocessor = preprocessor)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(41), 
                                     classNames = range(41),  
                                     saveFolder = saveFolder)

def createDataset_nopatches():
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/treesnopatches64'
    expectedDistribution = [0.35, 0.15, 0.5]

    imageSource = ImageDataSourceFactory.CreateResizingImageSource(
                      sourceFolder = sourceFolder,
                      newSize = 64, log=True, 
                      loadOnlyClasses=range(41))

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(41), 
                                     classNames = range(41),  
                                     saveFolder = saveFolder)
if __name__ == '__main__':
    #createDataset_halfToTest()
    createDataset_nopatches()
