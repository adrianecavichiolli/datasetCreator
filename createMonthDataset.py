from DatasetCreatorFactory import DatasetCreatorFactory
from ImageDataSourceFactory import ImageDataSourceFactory
from ConvnetBatchCreatorFactory import ConvnetBatchCreatorFactory
from PreprocessorFactory import PreprocessorFactory
from GetLabelFromFirstChars import GetLabelFromFirstChars
from ImageOps import grayscale


def createDataset_nopatches():
    sourceFolder  = '/home/gustavo/dev/bibliotecas/pylearn2/data/month-cropped-black'
    saveFolder = '/home/gustavo/dev/bibliotecas/pylearn2/data/month-cropped-black-nopatches'
    expectedDistribution = [0.5, 0.2, 0.3]

    imageSource = ImageDataSourceFactory.CreateResizingImageSource(
                      sourceFolder = sourceFolder,
                      log=True, 
                      newSize=20,
                      loadOnlyClasses=range(12),
                      grayScale=True)

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(12), 
                                     classNames = range(12),  
                                     saveFolder = saveFolder)


def createDataset_patches():
    sourceFolder  = '/home/gustavo/dev/bibliotecas/pylearn2/data/month-cropped-black'
    saveFolder = '/home/gustavo/dev/bibliotecas/pylearn2/data/month-cropped-black-patches'
    expectedDistribution = [0.5, 0.2, 0.3]

    preprocessor = PreprocessorFactory.CreateExtractGridPatches(20)

    imageSource = ImageDataSourceFactory.Create(
                      sourceFolder = sourceFolder,
                      log=True, 
                      loadOnlyClasses=range(12),
                      grayScale=True)

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource, 
                                                  preprocessor = preprocessor)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(12), 
                                     classNames = range(12),  
                                     saveFolder = saveFolder)

if __name__ == '__main__':
    #createDataset_halfToTest()
    createDataset_nopatches()
    #createDataset_patches()
