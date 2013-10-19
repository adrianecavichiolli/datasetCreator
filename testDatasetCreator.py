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

		
if __name__ == '__main__':
	unittest.main()
