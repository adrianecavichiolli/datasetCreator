from ClassBalancingDatasetSplitter import ClassBalancingDatasetSplitter
from DatasetCreator import DatasetCreator 

class DatasetCreatorFactory:
    @staticmethod
    def Create(imageSource):
        return DatasetCreator(imageSource = imageSource,
                              datasetSplitter =  ClassBalancingDatasetSplitter())
