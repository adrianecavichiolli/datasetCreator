import unittest
from DatasetCreator import DatasetCreator
from mock import Mock, call, MagicMock

class TestDatasetCreator(unittest.TestCase):
	def setUp(self):
		self.fileSystem = Mock()
		self.imageReader = Mock()
		self.batchBuilder = Mock()
		self.basefolder = 'basefolder'
		self.imageFolder = 'imgFolder'
		self.target = DatasetCreator(fileSystem = self.fileSystem, 
									 imageReader = self.imageReader,
									 batchBuilder = self.batchBuilder,
									 imageFolder = self.imageFolder,
									 saveFolder= self.basefolder)

	def test_singleImage(self):
		image = Mock()
		self.fileSystem.joinPath.return_value = 'basefolder/datasetName'
		self.fileSystem.listDir.return_value = ['file.jpg']
		self.fileSystem.isFile.return_value = True
		self.imageReader.read.return_value = image		
		
		self.target.CreateConvNet(name = 'datasetName')
		
		self.fileSystem.makeDir.assert_called_with('basefolder/datasetName')
		self.fileSystem.listDir.assert_called_with(self.imageFolder)
		self.imageReader.read.assert_called_with('imgFolder','file.jpg')
		self.batchBuilder.build.assert_called_with([image], 'basefolder/datasetName')

	def test_foldersAreIgnored(self):
		image = Mock()
		self.fileSystem.joinPath = MagicMock(side_effect = ['basefolder/datasetName', 'imgfolder/file.jpg', 'imgfolder/garbage'])
		self.fileSystem.listDir.return_value = ['file.jpg', 'garbage']
		self.fileSystem.isFile = MagicMock(side_effect = lambda x: x == 'imgfolder/file.jpg')
		self.imageReader.read.return_value = image		
		
		self.target.CreateConvNet(name = 'datasetName')
		
		self.imageReader.read.assert_called_with('imgFolder','file.jpg')
		
		
	def test_multipleImages(self):
		image = Mock()
		self.fileSystem.joinPath.return_value = 'basefolder/datasetName'
		self.fileSystem.listDir.return_value = ['file.jpg', 'file2.jpg', 'file3.jpg']
		self.fileSystem.isFile.return_value = True 
		self.imageReader.read.return_value = image
		
		self.target.CreateConvNet(name = 'datasetName')
		
		self.imageReader.read.assert_has_calls([call('imgFolder','file.jpg'), call('imgFolder','file2.jpg'), call('imgFolder','file3.jpg')])
		self.batchBuilder.build.assert_called_with([image, image, image], 'basefolder/datasetName')

if __name__ == '__main__':
	unittest.main()
