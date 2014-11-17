class ImageLoader:
    def __init__(self, ImageReader, Path, File):
        self.ImageReader = ImageReader
        self.Path = Path
        self.File = File

    def load(self):
        return self.ImageReader.read(self.Path, self.File)
