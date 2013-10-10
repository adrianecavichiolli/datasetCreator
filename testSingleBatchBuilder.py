import unittest
from mock import Mock
import numpy
from SingleBatchBuilder import SingleBatchBuilder 
from TestUtils import *

class testSingleBatchBuilder(unittest.TestCase):

	def test_singleImage(self):
		image = self.makeImage(numpy.arange(12), 0, 'file.jpg')
		
		expected = {}
		expected['data'] = arrayEqualsTo(numpy.arange(12).reshape(-1,1))
		expected['labels'] = [0]
		expected['filenames'] = ['file.jpg']
		
		serializer = Mock()
		target = SingleBatchBuilder(serializer)
		
		target.build([image], 'targetFolder/batch')
		
		serializer.write.assert_called_with('targetFolder/batch', expected)
		
	def test_multipleImages(self):
		image1 = self.makeImage(numpy.ones(12)*1, 0, 'file1.jpg')
		image2 = self.makeImage(numpy.ones(12)*2, 1, 'file2.jpg')
		image3 = self.makeImage(numpy.ones(12)*3, 2, 'file3.jpg')
		
		expected = {}
		data = numpy.asarray([numpy.ones(12), numpy.ones(12)*2, numpy.ones(12)*3]).T
		expected['data'] = arrayEqualsTo(data)
		expected['labels'] = [0,1,2]
		expected['filenames'] = ['file1.jpg','file2.jpg','file3.jpg']
		
		serializer = Mock()
		target = SingleBatchBuilder(serializer)
		
		target.build([image1, image2, image3], 'targetFolder/batch')
		
		serializer.write.assert_called_with('targetFolder/batch', expected)


	def makeImage(self, array, label, name):
		image = Mock()
		image.getArray.return_value = array
		image.getLabel.return_value = label
		image.getFilename.return_value = name
		return image

if __name__ == '__main__':
	unittest.main()
