import unittest
from DatasetCreator import DatasetCreator
from mock import Mock

class TestDatasetCreator(unittest.TestCase):
	def setUp(self):
		self.imageSource = Mock()
		self.datasetSplitter = Mock()
		self.target = DatasetCreator(self.imageSource, self.datasetSplitter)

	def test_ReadAndSplit(self):
		images = Mock()
		dataset = Mock()
		self.imageSource.load.return_value = images
		self.datasetSplitter.split.return_value = dataset
		
		classes = [0]
		result = self.target.buildDataset(classes = classes, datasetSplitIn = [.6, .2, .2])
		
		self.imageSource.load.assert_called_with()
		self.datasetSplitter.split.assert_called_with(images, [.6,.2,.2])
		self.assertEqual(dataset, result)

	def test_callsPreprocessorIfInformed(self):
		images = Mock()
		dataset = Mock()
		processedDataset = Mock()
		preprocessor = Mock()
		self.imageSource.load.return_value = images
		self.datasetSplitter.split.return_value = dataset
		preprocessor.process.return_value = processedDataset
		
		self.target = DatasetCreator(self.imageSource, self.datasetSplitter, preprocessor)
		
		classes = [0]
		result = self.target.buildDataset(classes = classes, datasetSplitIn = [.6, .2, .2])
		
		self.imageSource.load.assert_called_with()
		self.datasetSplitter.split.assert_called_with(images, [.6,.2,.2])
		preprocessor.process.assert_called_with(dataset)
		self.assertEqual(processedDataset, result)

		
if __name__ == '__main__':
	unittest.main()
