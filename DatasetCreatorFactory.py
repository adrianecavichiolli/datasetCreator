from ClassBalancingDatasetSplitter import ClassBalancingDatasetSplitter
from DatasetCreator import DatasetCreator 
from PredicateDatasetSplitter import PredicateDatasetSplitter
from FileGroupingDatasetSplitter import FileGroupingDatasetSplitter
from FileNumberRegexMatcher import FileNumberRegexMatcher
from GetSampleNumberFromFilename import GetSampleNumberFromFilename
from SampleGroupingDatasetSplitter import SampleGroupingDatasetSplitter

class DatasetCreatorFactory:
    @staticmethod
    def Create(imageSource, preprocessor = None):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter =  ClassBalancingDatasetSplitter(),
							  preprocessor = preprocessor)

    @staticmethod
    def CreateWithSplitter(imageSource, datasetSplitter, preprocessor = None):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter = datasetSplitter,
							  preprocessor = preprocessor)

    @staticmethod
    def CreateWithPredicateSplitter(imageSource, imgNumbersInValid, imgNumbersInTest, preprocessor = None):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter = PredicateDatasetSplitter(
                                  shouldBeInValid = FileNumberRegexMatcher(imgNumbersInValid),
                                  shouldBeInTest = FileNumberRegexMatcher(imgNumbersInTest)),
							  preprocessor = preprocessor)

    @staticmethod
    def CreateWithFileGroupingSplitter(imageSource, numFilePerImage, preprocessor = None):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter = FileGroupingDatasetSplitter(numFilePerImage),
							  preprocessor = preprocessor)

    @staticmethod
    def CreateWithSampleGroupingSplitter(imageSource, preprocessor = None, GetSampleNumberFunction = None):
        if GetSampleNumberFunction is None:
            GetSampleNumberFunction = GetSampleNumberFromFilename()
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter = SampleGroupingDatasetSplitter(GetSampleNumberFunction),
							  preprocessor = preprocessor)
