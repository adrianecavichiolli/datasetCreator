class DatasetCreator:
	def __init__(self, imageSource, datasetSplitter, preprocessor = None):
		self.imageSource = imageSource
		self.datasetSplitter = datasetSplitter
		self.preprocessor = preprocessor
		
	def buildDataset(self, datasetSplitIn = [0.6, 0.2, 0.2]):
		images = self.imageSource.load()

		dataset = self.datasetSplitter.split(images, datasetSplitIn)
		
		if self.preprocessor is not None:
			return self.preprocessor.process(dataset)
		else:
			return dataset