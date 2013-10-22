import unittest
from  ResizingImageDataSource import ResizingImageDataSource
from mock import Mock, call
from LabeledImage import LabeledImage

class testResizingImageDataSource(unittest.TestCase):
    def test_all(self):
        imageDataSource = Mock()
        imageResizer = Mock()
        
        imageDataSource.load.return_value = [self.makeImage(i,i) for i in [1,2,3,4]]
        imageResizer.resize.side_effect = [5, 6, 7, 8]
        target = ResizingImageDataSource(imageDataSource, imageResizer)

        results = target.load()
        
        imageDataSource.load.assert_called_with()
        imageResizer.resize.assert_has_calls([call(i) for i in [1,2,3,4]])
        self.assertEqual([5,6,7,8], [img.image for img in results])
        self.assertEqual([1,2,3,4], [img.label for img in results])
                                     
        
        
    def makeImage(self, image, label):
        return LabeledImage(image, 'dummy', label)
        
        
if __name__ == '__main__':
    unittest.main()
