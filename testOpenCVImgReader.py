import unittest
from OpencvImgReader import OpenCVImgReader
from mock import Mock
import numpy
from TestUtils import arrayEqualsTo


class testOpenCVImgReader(unittest.TestCase):
	def test_ReadImageSwapBGR_to_RGB(self):
		#openCV uses BGR order instead of RGB
		mockCv = Mock()
		imageFactory = Mock()
		fileSystem = Mock()
		
		fileSystem.joinPath.return_value = 'somefolder/somefile.jpg' 
		
		original = numpy.zeros((2,2,3))
		original[:,:,2] =  [[0,1], [2,3]]
		original[:,:,1] =  [[4,5], [6,7]]
		original[:,:,0] =  [[8,9], [10,11]]
		
		expected = numpy.zeros((2,2,3))
		expected[:,:,0] =  [[0,1], [2,3]]
		expected[:,:,1] =  [[4,5], [6,7]]
		expected[:,:,2] =  [[8,9], [10,11]]
		
		mockCv.imread = Mock()
		mockCv.imread.return_value = original
		target = OpenCVImgReader(imageFactory= imageFactory, fileSystem = fileSystem, openCV = mockCv)
		
		target.read('somefolder','somefile.jpg')
		
		fileSystem.joinPath.assert_called_with('somefolder','somefile.jpg')
		mockCv.imread.assert_called_with('somefolder/somefile.jpg')
		imageFactory.create.assert_called_with(arrayEqualsTo(expected), 'somefile.jpg')
		
		
if __name__ == '__main__':
	unittest.main()
