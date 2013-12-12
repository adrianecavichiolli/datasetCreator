from ImageDataSource import ImageDataSource
from Filesystem import FileSystem
from OpencvImgReader import OpenCVImgReader
from GrayscaleOpencvImgReader import GrayscaleOpenCVImgReader
from ImageFactory import LabeledImageFactory
from ResizingImageReader import ResizingImageReader
from SquaredImageResizer import SquaredImageResizer
from OpencvImageResizer import OpencvImageResizer
from TextLogger import TextLogger
from LabelInFilenamePredicate import LabelInFilenamePredicate
from GetLabelFromFirstChars import GetLabelFromFirstChars
import cv2

class ImageDataSourceFactory:
    @staticmethod
    def Create(sourceFolder, log = False,  loadOnlyClasses = None, grayScale = False, getLabelFunction = None):
        return ImageDataSourceFactory.CreateWithImageReader(
                            ImageDataSourceFactory.__CreateStandardImageReader(grayScale, getLabelFunction),
                            sourceFolder, log, loadOnlyClasses, getLabelFunction)

    @staticmethod
    def CreateResizingImageSource(sourceFolder, newSize, log = False, loadOnlyClasses = None, grayScale = False, getLabelFunction = None ):
        return ImageDataSourceFactory.CreateWithImageReader(
                            ImageDataSourceFactory.__CreateResizingImageReader(
                                        ImageDataSourceFactory.__CreateStandardImageReader(grayScale, getLabelFunction),
                                        newSize),
                            sourceFolder, log, loadOnlyClasses, getLabelFunction)

    
    @staticmethod
    def CreateWithImageReader(imageReader, sourceFolder, log = False, loadOnlyClasses = None, getLabelFunction = None):
        if getLabelFunction is None:
            getLabelFunction = GetLabelFromFirstChars(nChars=2)
        imageDataSource =  ImageDataSource(fileSystem = FileSystem(),
                              imageReader = imageReader,
                              sourceFolder = sourceFolder)
                              
        if log:
            imageDataSource.setLogger(TextLogger())
        if loadOnlyClasses is not None:
            imageDataSource.setFilenamePredicate(LabelInFilenamePredicate(getLabelFunction, loadOnlyClasses))
        return imageDataSource
        
    @staticmethod
    def __CreateStandardImageReader(grayScale, getLabelFunction):
        if getLabelFunction is None:
            getLabelFunction = GetLabelFromFirstChars(nChars=2)
        
        if (not grayScale):
            return OpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, grayScale),
                                   openCV = cv2, 
                                   fileSystem = FileSystem())
        else:
            return GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, grayScale),
                           openCV = cv2, 
                           fileSystem = FileSystem())
    
    @staticmethod
    def __CreateResizingImageReader(imageReader, newSize):
        return ResizingImageReader(imageReader =  imageReader,
                                   imageResizer = SquaredImageResizer(OpencvImageResizer(), newSize))