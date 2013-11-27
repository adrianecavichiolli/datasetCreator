import unittest
from GrayscaleOpencvImgReader import GrayscaleOpenCVImgReader 
from mock import Mock, MagicMock, PropertyMock
import numpy
from TestUtils import arrayEqualsTo


class testOpenCVImgReader(unittest.TestCase):
	def test_calledWithGrayscaleflag(self):
		#openCV uses BGR order instead of RGB
		mockCv = MagicMock()
		GRAYSCALE = Mock()
		type(mockCv).CV_LOAD_IMAGE_GRAYSCALE = PropertyMock(return_value=GRAYSCALE)
		imageFactory = Mock()
		fileSystem = Mock()
		
		fileSystem.joinPath.return_value = 'somefolder/somefile.jpg' 
		
		image = Mock()
		mockCv.imread = Mock()
		mockCv.imread.return_value = image
		target = GrayscaleOpenCVImgReader(imageFactory= imageFactory, fileSystem = fileSystem, openCV = mockCv)
		
		target.read('somefolder','somefile.jpg')
		
		fileSystem.joinPath.assert_called_with('somefolder','somefile.jpg')
		mockCv.imread.assert_called_with('somefolder/somefile.jpg', GRAYSCALE)
		imageFactory.create.assert_called_with(image, 'somefile.jpg')
		
		
if __name__ == '__main__':
	unittest.main()
