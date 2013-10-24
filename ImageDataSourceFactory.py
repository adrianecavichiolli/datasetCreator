from ImageDataSource import ImageDataSource
from Filesystem import FileSystem
from OpencvImgReader import OpenCVImgReader
from ImageFactory import LabeledImageFactory
from ResizingImageReader import ResizingImageReader
from SquaredImageResizer import SquaredImageResizer
from OpencvImageResizer import OpencvImageResizer
from TextLogger import TextLogger
from LabelInFilenamePredicate import LabelInFilenamePredicate
import cv2

class ImageDataSourceFactory:
    @staticmethod
    def Create(sourceFolder, log = False,  loadOnlyClasses = None):
        return ImageDataSourceFactory.CreateWithImageReader(
                            ImageDataSourceFactory.__CreateStandardImageReader(),
                            sourceFolder, log, loadOnlyClasses)

    @staticmethod
    def CreateResizingImageSource(sourceFolder, newSize, log = False, loadOnlyClasses = None):
        return ImageDataSourceFactory.CreateWithImageReader(
                            ImageDataSourceFactory.__CreateResizingImageReader(newSize),
                            sourceFolder, log, loadOnlyClasses)

    
    @staticmethod
    def CreateWithImageReader(imageReader, sourceFolder, log = False, loadOnlyClasses = None):
        imageDataSource =  ImageDataSource(fileSystem = FileSystem(),
                              imageReader = imageReader,
                              sourceFolder = sourceFolder)
                              
        if log:
            imageDataSource.setLogger(TextLogger())
        if loadOnlyClasses is not None:
            imageDataSource.setFilenamePredicate(LabelInFilenamePredicate(loadOnlyClasses))
        return imageDataSource
        
    @staticmethod
    def __CreateStandardImageReader():
        return OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem())
    
    @staticmethod
    def __CreateResizingImageReader(newSize):
        imageReader = ImageDataSourceFactory.__CreateStandardImageReader()
        return ResizingImageReader(imageReader =  imageReader,
                                   imageResizer = SquaredImageResizer(OpencvImageResizer(), newSize))