class DatasetCreator:
	def __init__(self, imageSource, datasetSplitter):
		self.imageSource = imageSource
		self.datasetSplitter = datasetSplitter
		
	def buildDataset(self, classes, datasetSplitIn = [0.6, 0.2, 0.2]):
		images = self.imageSource.load()

		return self.datasetSplitter.split(images, datasetSplitIn)
