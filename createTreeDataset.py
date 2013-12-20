from DatasetCreatorFactory import DatasetCreatorFactory
from ImageDataSourceFactory import ImageDataSourceFactory
from ConvnetBatchCreatorFactory import ConvnetBatchCreatorFactory
from PreprocessorFactory import PreprocessorFactory
from GetLabelFromFirstChars import GetLabelFromFirstChars
from ImageOps import grayscale


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
    sourceFolder = '/home/especial/vri/databases/florestais-macro'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/treesnopatches256_3'
    expectedDistribution = [0.35, 0.15, 0.5]

    imageSource = ImageDataSourceFactory.CreateResizingImageSource(
                      sourceFolder = sourceFolder,
                      newSize = 256, log=True, 
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
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/treesmicro_640_50train_3'
    expectedDistribution = [0.5, 0.2, 0.3]

    imageSource = ImageDataSourceFactory.CreateResizingImageSource(
                      sourceFolder = sourceFolder,
                      newSize = 640, log=True,
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
    createDataset_nopatches()
    #createDatasetMicro_nopatches()
