import unittest
from  ImageReaderDecorator import ImageReaderDecorator
from mock import Mock, call
from LabeledImage import LabeledImage

class testImageReaderDecorator(unittest.TestCase):
    def test_all(self):
        imageReader = Mock()
        
        originalImage = LabeledImage(Mock(), 'filename', 0)
        resizedImage = Mock()
        imageReader.read.return_value = originalImage
        decorator = Mock(return_value = resizedImage)
        
        target = ImageReaderDecorator(imageReader, decorator)

        result = target.read('source', 'myfile.jpg')
        
        imageReader.read.assert_called_with('source', 'myfile.jpg')
        self.assertEqual(result.image, resizedImage)       
        
if __name__ == '__main__':
    unittest.main()
