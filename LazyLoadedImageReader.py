from ImageLoader import ImageLoader

class LazyLoadedImageReader:
    def __init__(self, imageReader, lazyImageFactory):
        self.imageReader = imageReader
        self.lazyImageFactory = lazyImageFactory
    
    def read(self, path, filename):
        loader = ImageLoader(self.imageReader, path, filename)
        return self.lazyImageFactory.create(loader, filename)
