from DatasetCreatorFactory import DatasetCreatorFactory
from ImageDataSourceFactory import ImageDataSourceFactory
from ConvnetBatchCreatorFactory import ConvnetBatchCreatorFactory
from PreprocessorFactory import PreprocessorFactory
from GetLabelFromFirstChars import GetLabelFromFirstChars
from GrayscaleOpencvImgReader import GrayscaleOpenCVImgReader
from ImageReaderDecorator import ImageReaderDecorator
from ImageOps import grayscale
from ImageFactory import LabeledImageFactory
from GetLabelFromFirstChars import GetLabelFromFirstChars
import cv2
from ImageInverter import ImageInverter
from Filesystem import FileSystem


def createDatasetBFL_256():
    sourceFolder = '/home/especial/vri/databases/autoria/BFL'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/BFL_64'
    expectedDistribution = [0.5, 0.2, 0.3]


    getLabelFunction = GetLabelFromFirstChars(nChars=3)
    imageReader = GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, True),
                           openCV = cv2, 
                           fileSystem = FileSystem())

    imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = imageReader,
                      sourceFolder = sourceFolder,
                      log=True, 
                      getLabelFunction = getLabelFunction)

    datasetCreator = DatasetCreatorFactory.CreateWithPredicateSplitter(
                            imageSource = imageSource,
                            imgNumbersInValid = range(10,19),
                            imgNumbersInTest = range(19,28))

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(315), 
                                     classNames = range(315),  
                                     saveFolder = saveFolder)

def createDatasetBFL_bin_256():
    sourceFolder = '/home/especial/vri/databases/autoria/BFL_binary'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/BFL_binary'
    expectedDistribution = [0.5, 0.2, 0.3]


    getLabelFunction = GetLabelFromFirstChars(nChars=3)
    imageReader = GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, True),
                           openCV = cv2, 
                           fileSystem = FileSystem())

    imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = imageReader,
                      sourceFolder = sourceFolder,
                      log=True, 
                      getLabelFunction = getLabelFunction)

    datasetCreator = DatasetCreatorFactory.CreateWithFileGroupingSplitter(imageSource = imageSource,
                                                    numFilePerImage = 9)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(315), 
                                     classNames = range(315),  
                                     saveFolder = saveFolder)

def createDatasetBFL_256_inv():
    sourceFolder = '/home/especial/vri/databases/autoria/BFL'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/BFL_64_inv_split'
    expectedDistribution = [0.5, 0.2, 0.3]


    getLabelFunction = GetLabelFromFirstChars(nChars=3)
    imageReader = GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, True),
                           openCV = cv2, 
                           fileSystem = FileSystem())

    invertingImageReader = ImageReaderDecorator(imageReader =  imageReader,
                                   decorator = ImageInverter())

    imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = invertingImageReader,
                      sourceFolder = sourceFolder,
                      log=True, 
                      getLabelFunction = getLabelFunction)

    datasetCreator = DatasetCreatorFactory.CreateWithFileGroupingSplitter(imageSource = imageSource,
                                                    numFilePerImage = 9)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(315), 
                                     classNames = range(315),  
                                     saveFolder = saveFolder)
    
def createDatasetIAM():
    sourceFolder = '/home/especial/vri/databases/autoria/IAM'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/IAM_orig'
    expectedDistribution = [0.5, 0.2, 0.3]

    getLabelFunction = GetLabelFromFirstChars(nChars=3)
    imageReader = GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, True),
                           openCV = cv2, 
                           fileSystem = FileSystem())

    invertingImageReader = ImageReaderDecorator(imageReader =  imageReader,
                                   decorator = ImageInverter())

    imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = invertingImageReader,
                      sourceFolder = sourceFolder,
                      log=True, 
                      getLabelFunction = getLabelFunction)

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(672), 
                                     classNames = range(672),  
                                     saveFolder = saveFolder)

if __name__ == '__main__':
    createDatasetBFL_256_inv()
    #createDatasetIAM()
