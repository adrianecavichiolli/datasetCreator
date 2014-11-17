from LazyLoadedImage  import LazyLoadedImage

class LazyLoadedImageFactory:
    def __init__(self, getLabelFunction, grayscale, verbose):
        self.getLabelFunction = getLabelFunction
        self.grayscale = grayscale
        self.verbose = verbose
		
    def create(self, loader, filename):
        return LazyLoadedImage(loader, filename, self.getLabelFunction(filename), self.grayscale, self.verbose)
