class ResizingImageDataSource:
    def __init__(self, imageDataSource, imageResizer):
        self.imageDataSource = imageDataSource
        self.imageResizer = imageResizer
    
    def load(self):
        images = self.imageDataSource.load()
        map(self.resizeImage, images)
        return images
    
    def resizeImage(self, image):
        image.image = self.imageResizer.resize(image.image)