from  DatasetSplitter import DatasetSplitter
from DatasetCreator import DatasetCreator 

class DatasetCreatorFactory:
    @staticmethod
    def Create(imageSource):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter = DatasetSplitter())
