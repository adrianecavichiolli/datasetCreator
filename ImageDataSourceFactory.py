from ImageDataSource import ImageDataSource
from Filesystem import FileSystem
from OpencvImgReader import OpenCVImgReader
from ImageFactory import LabeledImageFactory
from ResizingImageDataSource import ResizingImageDataSource
from SquaredImageResizer import SquaredImageResizer
from OpencvImageResizer import OpencvImageResizer
import cv2

class ImageDataSourceFactory:
    @staticmethod
    def Create(sourceFolder):
        return ImageDataSource(fileSystem = FileSystem(),
                              imageReader = OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem()),
                              sourceFolder = sourceFolder)

    @staticmethod
    def CreateResizingImageSource(sourceFolder, newSize):
        imageDataSource = ImageDataSourceFactory.Create(sourceFolder)
        return ResizingImageDataSource(imageDataSource = imageDataSource,
                                       imageResizer = SquaredImageResizer(OpencvImageResizer(), newSize))