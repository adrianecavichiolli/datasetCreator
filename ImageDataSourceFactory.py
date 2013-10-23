from ImageDataSource import ImageDataSource
from Filesystem import FileSystem
from OpencvImgReader import OpenCVImgReader
from ImageFactory import LabeledImageFactory
from ResizingImageDataSource import ResizingImageDataSource
from SquaredImageResizer import SquaredImageResizer
from OpencvImageResizer import OpencvImageResizer
from TextLogger import TextLogger
from LabelInFilenamePredicate import LabelInFilenamePredicate
import cv2

class ImageDataSourceFactory:
    @staticmethod
    def Create(sourceFolder, loadOnlyClasses = None, log = False):
        logger = TextLogger() if log else None
        if loadOnlyClasses is None:
            predicate = lambda x: True
        else:
            predicate = LabelInFilenamePredicate(loadOnlyClasses)
        return ImageDataSource(fileSystem = FileSystem(),
                              imageReader = OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem()),
                              sourceFolder = sourceFolder,
                              logger = logger,
                              loadImagesMatching = predicate)

    @staticmethod
    def CreateResizingImageSource(sourceFolder, newSize, loadOnlyClasses = None, log = False):
        imageDataSource = ImageDataSourceFactory.Create(sourceFolder, loadOnlyClasses, log)
        return ResizingImageDataSource(imageDataSource = imageDataSource,
                                       imageResizer = SquaredImageResizer(OpencvImageResizer(), newSize))