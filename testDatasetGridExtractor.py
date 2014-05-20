import unittest
from mock import Mock, call
from DatasetGridExtractor import DatasetGridExtractor
from LabeledImage import LabeledImage
import numpy


class testDatasetGridExtractor(unittest.TestCase):
    def testSplitDataset(self):
        img1 = numpy.zeros((200,300))
        expected = [numpy.ones((100,100)) * 0,
                    numpy.ones((100,100)) * 1,
                    numpy.ones((100,100)) * 2,
                    numpy.ones((100,100)) * 3,
                    numpy.ones((100,100)) * 4,
                    numpy.ones((100,100)) * 5]

        img1[100*0:100*1,100*0:100*1] = expected[0]
        img1[100*0:100*1,100*1:100*2] = expected[1]  
        img1[100*0:100*1,100*2:100*3] = expected[2]    
        img1[100*1:100*2,100*0:100*1] = expected[3] 
        img1[100*1:100*2,100*1:100*2] = expected[4]   
        img1[100*1:100*2,100*2:100*3] = expected[5]     

        oneset = [self.createImage(img1)]
        dataset = (oneset, oneset, oneset)

        target = DatasetGridExtractor(numRows = 2, numCols = 3)
        result = target.run(dataset)

        imageResults1 = [item[0].image for item in result[0]]
        imageResults2 = [item[0].image for item in result[1]]
        imageResults3 = [item[0].image for item in result[2]]
        numpy.testing.assert_array_equal(imageResults1, expected)
        numpy.testing.assert_array_equal(imageResults2, expected)
        numpy.testing.assert_array_equal(imageResults3, expected)


    def createImage(self, img, label=0, filename=""):
        image = LabeledImage(img, filename, label)
        return image

if __name__ == '__main__':
    unittest.main()
