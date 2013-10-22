import unittest
from mock import Mock
from MetaBatchBuilder import MetaBatchBuilder
import numpy
from TestUtils import arrayEqualsTo

class testMetaBatchBuilder(unittest.TestCase):
	def test_all(self):

		target = MetaBatchBuilder()
		
		
		train = [self.makeImage([10, 20, 40, 80]),
				   self.makeImage([20, 40, 40, 60])]
		valid = [self.makeImage([10, 20, 40, 80]),
				   self.makeImage([20, 40, 40, 60])]
		test = [self.makeImage([1000, 2000, 4000, 8000]),
				   self.makeImage([2000, 4000, 4000, 6000])]
		
		dataset = (train, valid, test)
		classesNames = 'myname'
		
		expected = {}
		expected['num_vis'] = 4
		expected['data_in_rows']  = True
		expected['label_names'] = classesNames
		expected['data_mean'] = arrayEqualsTo(numpy.asarray([15, 30, 40, 70]).reshape(-1,1))

		self.assertEqual(expected, target.build(dataset, classesNames))
	

	def makeImage(self, array):
		image = Mock()
		image.getArray.return_value = numpy.asarray(array)
		return image

if __name__ == '__main__':
	unittest.main()
