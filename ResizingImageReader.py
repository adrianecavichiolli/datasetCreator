class ResizingImageReader:
    def __init__(self, imageReader, imageResizer):
        self.imageReader = imageReader
        self.imageResizer = imageResizer
    
    def read(self, path, filename):
        image = self.imageReader.read(path, filename)
        return image.createCopyWithImage(self.imageResizer.resize(image.image))