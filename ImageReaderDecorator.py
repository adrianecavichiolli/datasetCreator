class ImageReaderDecorator:
    def __init__(self, imageReader, decorator):
        self.imageReader = imageReader
        self.decorator = decorator
    
    def read(self, path, filename):
        image = self.imageReader.read(path, filename)
        return image.createCopyWithImage(self.decorator(image.image))
