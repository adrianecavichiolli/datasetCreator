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

class DatasetCreatorFactory:
    @staticmethod
    def create(imgFolder, saveFolder, randomNumberGenerator = random.Random):
        return DatasetCreator(fileSystem = FileSystem(),
							  imageReader = OpenCVImgReader(imageFactory = LabeledImageFactory(), openCV = cv2, fileSystem = FileSystem()),
							  batchBuilder = BatchBuilder(SingleBatchBuilder(cPickleSerializer())),
							  imageFolder = imgFolder,
							  saveFolder = saveFolder)
