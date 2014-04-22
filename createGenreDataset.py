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
from PercentageImageResizer import PercentageImageResizer
from OpencvImageResizer import OpencvImageResizer



def createDatasetGenre_point6():
    sourceFolder = '/home/especial/vri/databases/generos_musicais/classinname'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/Genre_60percent'
    expectedDistribution = [0.5, 0.2, 0.3]

    getLabelFunction = GetLabelFromFirstChars(nChars=2)
    imageReader = GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, True),
                           openCV = cv2, 
                           fileSystem = FileSystem())

    resizingImageReader = ImageReaderDecorator(imageReader =  imageReader,
                                    decorator = PercentageImageResizer(OpencvImageResizer(), 0.6))

    imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = resizingImageReader,
                      sourceFolder = sourceFolder,
                      log=True, 
                      getLabelFunction = getLabelFunction)


    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(10), 
                                     classNames = range(10),  
                                     saveFolder = saveFolder)

if __name__ == '__main__':
    createDatasetGenre_point6()

