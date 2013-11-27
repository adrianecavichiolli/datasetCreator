from DatasetCreatorFactory import DatasetCreatorFactory
from ImageDataSourceFactory import ImageDataSourceFactory
from ConvnetBatchCreatorFactory import ConvnetBatchCreatorFactory
from PreprocessorFactory import PreprocessorFactory
from GetLabelFromFirstChars import GetLabelFromFirstChars
from ImageOps import grayscale

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
    

def createDatasetMicro_nopatches():
    sourceFolder = '/home/especial/vri/databases/florestais-micro'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/treesmicro_640'
    expectedDistribution = [0.35, 0.15, 0.5]

    imageSource = ImageDataSourceFactory.CreateResizingImageSource(
                      sourceFolder = sourceFolder,
                      newSize = 640, log=True,
                      loadOnlyClasses=range(112),
                      getLabelFunction = GetLabelFromFirstChars(nChars=3),
                      grayScale = True)

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(112), 
                                     classNames = range(112),  
                                     saveFolder = saveFolder)
if __name__ == '__main__':
    #createDataset_halfToTest()
    #createDataset_nopatches()
    createDatasetMicro_nopatches()
