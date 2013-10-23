import unittest
from mock import Mock, MagicMock, call
from ImageDataSource import ImageDataSource

class testImageDataSource(unittest.TestCase):
    
    def setUp(self):
        self.fileSystem = Mock()
        self.imageReader = Mock()
        self.fileSystem.joinPath = MagicMock(side_effect = lambda x,y: x + '/' + y)
        self.sourceFolder = 'source'
        self.target = ImageDataSource(fileSystem = self.fileSystem, imageReader = self.imageReader, sourceFolder = self.sourceFolder)
    
    def testLoadImages(self):       
        image = Mock()
        
        self.fileSystem.listDir.return_value = ['file.jpg']
        self.fileSystem.isFile.return_value = True
        self.imageReader.read.return_value = image
        
        images = self.target.load()
        
        self.fileSystem.listDir.assert_called_with(self.sourceFolder)
        self.imageReader.read.assert_called_with(self.sourceFolder,'file.jpg')
        self.assertEqual(images, [image])

    def test_foldersAreIgnored(self):
        image = Mock()
        self.fileSystem.listDir.return_value = ['file.jpg', 'garbage']
        self.fileSystem.isFile = MagicMock(side_effect = lambda x: x == '%s/file.jpg' %self.sourceFolder)
        self.imageReader.read.return_value = image        
        
        self.target.load()
        
        self.imageReader.read.assert_called_with(self.sourceFolder,'file.jpg')
        
    def test_multipleImages(self):
        image = Mock()
        self.fileSystem.listDir.return_value = ['file.jpg', 'file2.jpg', 'file3.jpg']
        self.fileSystem.isFile.return_value = True 
        self.imageReader.read.return_value = image
        
        images = self.target.load()
        
        self.imageReader.read.assert_has_calls([call(self.sourceFolder,'file.jpg'), call(self.sourceFolder,'file2.jpg'), call(self.sourceFolder,'file3.jpg')])
        self.assertEqual(images, [image, image, image])

    def test_writesToLog_ifLoggerIsInformed(self):
        logger = Mock()
        self.fileSystem.listDir.return_value = ['file.jpg', 'file2.jpg', 'file3.jpg']
        self.fileSystem.isFile.return_value = True 
        self.imageReader.read.return_value = Mock()
        
        target = ImageDataSource(fileSystem = self.fileSystem, 
                                 imageReader = self.imageReader, 
                                 sourceFolder = self.sourceFolder,
                                 logger = logger)
        target.load()
        
        logger.log.assert_has_calls([call('Reading file %s' % name) for name in ['file.jpg', 'file2.jpg', 'file3.jpg']])
