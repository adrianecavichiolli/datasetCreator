class ResizingImageDataSource:
    def __init__(self, imageDataSource, imageResizer):
        self.imageDataSource = imageDataSource
        self.imageResizer = imageResizer
    
    def load(self):
        return [self.resizeImage(img) for img in self.imageDataSource.load()]
    
    def resizeImage(self, image):
        return image.createCopyWithImage(self.imageResizer.resize(image.image))