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
from GetLabelFromLookup import *
import cv2
from ImageInverter import ImageInverter
from Filesystem import FileSystem
from PercentageImageResizer import PercentageImageResizer
from OpencvImageResizer import OpencvImageResizer


def getBrodatzClasses():
    return ['bark', 'beachsand', 'beans', 'burlap', 'd10', 'd11', 'd4', 'd5', 'd51',
 'd52', 'd6', 'd95', 'fieldstone', 'grass', 'ice', 'image09', 'image15', 'image17',
 'image19', 'paper', 'peb54', 'pigskin', 'pressedcl', 'raffia', 'raffia2',
 'reptile', 'ricepaper', 'seafan', 'straw2', 'tree', 'water', 'woodgrain']


def createDatasetBrodatz():
    sourceFolder = '/home/especial/vri/databases/brodatz/as_png'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/brodatz'
    expectedDistribution = [0.3, 0.2, 0.5]

    classNames = getBrodatzClasses()
    getLabelFunction = GetLabelFromLookup(classNames = classNames, separator = "_")

    imageSource = ImageDataSourceFactory.Create(
                      sourceFolder = sourceFolder,
                      log=True, 
                      grayScale = True,
                      getLabelFunction = getLabelFunction)


    datasetCreator = DatasetCreatorFactory.CreateWithSampleGroupingSplitter(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(len(classNames)), 
                                     classNames = classNames,  
                                     saveFolder = saveFolder)

if __name__ == '__main__':
    createDatasetBrodatz()

