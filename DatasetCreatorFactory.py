import random
import os
import cv2
from Filesystem import FileSystem
from ImageFactory import LabeledImageFactory
from OpencvImgReader import OpenCVImgReader
from BatchBuilder import BatchBuilder
from SingleBatchBuilder import SingleBatchBuilder
from DatasetCreator import DatasetCreator
from cPickleSerializer import cPickleSerializer
from MetaBatchBuilder import MetaBatchBuilder
from BatchRepository import BatchRepository

class DatasetCreatorFactory:
    @staticmethod
    def create(imgFolder, saveFolder, classNames, randomNumberGenerator = random.Random):
        return DatasetCreator(fileSystem = FileSystem(),
							  imageReader = OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem()),
							  batchBuilder = BatchBuilder(SingleBatchBuilder(),MetaBatchBuilder()),
                              batchRepository = BatchRepository(fileSystem = FileSystem(), serializer = cPickleSerializer()),
							  imageFolder = imgFolder,
							  saveFolder = saveFolder,
							  classNames = classNames)
