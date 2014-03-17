from ClassBalancingDatasetSplitter import ClassBalancingDatasetSplitter
from DatasetCreator import DatasetCreator 
from PredicateDatasetSplitter import PredicateDatasetSplitter
from FileNumberRegexMatcher import FileNumberRegexMatcher

class DatasetCreatorFactory:
    @staticmethod
    def Create(imageSource, preprocessor = None):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter =  ClassBalancingDatasetSplitter(),
							  preprocessor = preprocessor)

    @staticmethod
    def CreateWithPredicateSplitter(imageSource, imgNumbersInValid, imgNumbersInTest, preprocessor = None):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter = PredicateDatasetSplitter(
                                  shouldBeInValid = FileNumberRegexMatcher(imgNumbersInValid),
                                  shouldBeInTest = FileNumberRegexMatcher(imgNumbersInTest)),
							  preprocessor = preprocessor)
