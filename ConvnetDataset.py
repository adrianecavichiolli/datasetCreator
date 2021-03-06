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
from OpencvImgReader import OpenCVImgReader
from GetSampleNumberFromFilename import GetSampleNumberFromFilename
from ClassBalancingDatasetSplitter import ClassBalancingDatasetSplitter
from SquaredImageResizer import SquaredImageResizer
from GetLabelFromLookup import GetLabelFromLookup
from SampleGroupingDatasetSplitter import SampleGroupingDatasetSplitter
from FileGroupingDatasetSplitter import FileGroupingDatasetSplitter
from FixedDatasetSplitter import FixedDatasetSplitter

from LazyLoadedImageReader import LazyLoadedImageReader
from LazyLoadedImageFactory import LazyLoadedImageFactory
from ImageLoader import ImageLoader

#Functions to get the label from a filename
def LabelFromFirstChars(nChars):
    return GetLabelFromFirstChars(nChars)

def LabelFromList(listOfNames, separator = "_"):
    return GetLabelFromLookup(listOfNames, separator)

#Functions to Resize the images
def ResizeByPercent(percent):
    return PercentageImageResizer(OpencvImageResizer(), percent)

def ResizeToSquare(newSize):
    return SquaredImageResizer(OpencvImageResizer(), newSize)

#Functions to split the dataset
def ClassBalancingSplit():
    return ClassBalancingDatasetSplitter()

def GroupingSplit(GetSampleNumberFunction = None):
    if GetSampleNumberFunction is None:
        GetSampleNumberFunction = GetSampleNumberFromFilename()

    return SampleGroupingDatasetSplitter(GetSampleNumberFunction)

def FileGroupingSplit(numFilePerImage, shuffle=True):
    return FileGroupingDatasetSplitter(numFilePerImage, shuffle)

def SplitUsingFixedList(files_in_train, files_in_valid, files_in_test):
    return FixedDatasetSplitter(files_in_train, files_in_train, files_in_test)

#Preprocessors
def ExtractGridPatches(patchSize):
    return PreprocessorFactory.CreateExtractGridPatches(patchSize)


class ConvnetDataset:
    @staticmethod
    def CreateConvNetDataset(SourceFolder, TargetFolder, ExpectedDistribution, Classes, ClassNames,
                GetLabelsFrom = LabelFromFirstChars(2), 
                Grayscale = False, InvertColor = False, ResizeBy = None,
                Preprocessor = None, SplitFunction = ClassBalancingSplit(), NumTrainBatches = 3, Log  = True,
                LazyLoadedImages = False):
        dataset = ConvnetDataset.CreateDataset(SourceFolder, TargetFolder, ExpectedDistribution, Classes,
                                                ClassNames, GetLabelsFrom, Grayscale, InvertColor, ResizeBy, Preprocessor,
                                                SplitFunction, NumTrainBatches, Log, LazyLoadedImages)
        convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = NumTrainBatches)
        
        convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = Classes,
                                     classNames = ClassNames,
                                     saveFolder = TargetFolder)

    @staticmethod
    def CreateDataset(SourceFolder, TargetFolder, ExpectedDistribution, Classes, ClassNames,
                GetLabelsFrom = LabelFromFirstChars(2), 
                Grayscale = False, InvertColor = False, ResizeBy = None,
                Preprocessor = None, SplitFunction = ClassBalancingSplit(), NumTrainBatches = 3, Log  = True, 
                LazyLoadedImages = False):

        if Grayscale:
            imageReader = GrayscaleOpenCVImgReader(
                           imageFactory = LabeledImageFactory(GetLabelsFrom, Grayscale),
                           openCV = cv2, 
                           fileSystem = FileSystem())
        else:
            imageReader = OpenCVImgReader(
                           imageFactory = LabeledImageFactory(GetLabelsFrom, Grayscale),
                           openCV = cv2, 
                           fileSystem = FileSystem())

        if InvertColor:
            imageReader = ImageReaderDecorator(imageReader =  imageReader,
                                   decorator = ImageInverter())
        
        if ResizeBy is not None:
            imageReader = ImageReaderDecorator(imageReader =  imageReader,
                                   decorator = ResizeBy)

        if LazyLoadedImages:
            lazyImageFactory = LazyLoadedImageFactory(GetLabelsFrom, Grayscale, Log)
            imageReader = LazyLoadedImageReader(imageReader, lazyImageFactory)


        imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = imageReader,
                      sourceFolder = SourceFolder,
                      log = Log,
                      loadOnlyClasses = Classes,
                      getLabelFunction = GetLabelsFrom)


        datasetCreator = DatasetCreatorFactory.CreateWithSplitter(
                            imageSource = imageSource, 
                            datasetSplitter = SplitFunction,
                            preprocessor = Preprocessor)

        return datasetCreator.buildDataset(datasetSplitIn = ExpectedDistribution)

