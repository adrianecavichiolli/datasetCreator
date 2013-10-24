import unittest
from  ResizingImageReader import ResizingImageReader
from mock import Mock, call
from LabeledImage import LabeledImage

class testResizingImageReader(unittest.TestCase):
    def test_all(self):
        imageReader = Mock()
        imageResizer = Mock()
        
        originalImage = LabeledImage(Mock(), 'filename', 0)
        resizedImage = Mock()
        imageReader.read.return_value = originalImage
        imageResizer.resize.return_value = resizedImage
        
        target = ResizingImageReader(imageReader, imageResizer)

        result = target.read('source', 'myfile.jpg')
        
        imageReader.read.assert_called_with('source', 'myfile.jpg')
        imageResizer.resize.assert_called_with(originalImage.image)
        self.assertEqual(result.image, resizedImage)       
        
if __name__ == '__main__':
    unittest.main()
