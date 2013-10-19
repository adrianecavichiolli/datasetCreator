from ImageDataSource import ImageDataSource
from Filesystem import FileSystem
from OpencvImgReader import OpenCVImgReader
from ImageFactory import LabeledImageFactory
import cv2

class ImageDataSourceFactory:
    @staticmethod
    def Create(sourceFolder):
        return ImageDataSource(fileSystem = FileSystem(),
                              imageReader = OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem()),
                              sourceFolder = sourceFolder)
