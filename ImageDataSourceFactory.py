from ImageDataSource import ImageDataSource
from Filesystem import FileSystem
from OpencvImgReader import OpenCVImgReader
from ImageFactory import LabeledImageFactory
from ResizingImageDataSource import ResizingImageDataSource
from SquaredImageResizer import SquaredImageResizer
from OpencvImageResizer import OpencvImageResizer
from TextLogger import TextLogger
import cv2

class ImageDataSourceFactory:
    @staticmethod
    def Create(sourceFolder, log = False):
        if log:
            logger = TextLogger()
        else:
            logger = None
        return ImageDataSource(fileSystem = FileSystem(),
                              imageReader = OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem()),
                              sourceFolder = sourceFolder,
                              logger = logger)

    @staticmethod
    def CreateResizingImageSource(sourceFolder, newSize, log = False):
        imageDataSource = ImageDataSourceFactory.Create(sourceFolder, log)
        return ResizingImageDataSource(imageDataSource = imageDataSource,
                                       imageResizer = SquaredImageResizer(OpencvImageResizer(), newSize))