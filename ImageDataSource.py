class ImageDataSource:
    def __init__(self, fileSystem, imageReader, sourceFolder, logger = None, loadImagesMatching = lambda x:True):
        self.fileSystem = fileSystem
        self.imageReader = imageReader
        self.sourceFolder = sourceFolder
        self.logger = logger
        self.shouldLoadImage = loadImagesMatching
    
    def load(self):
        images = [self.ReadImage(img) 
                  for img in self.fileSystem.listDir(self.sourceFolder)
                  if self.fileSystem.isFile(self.fileSystem.joinPath(self.sourceFolder,img)) 
                  and self.shouldLoadImage(img)]
        return images

    def ReadImage(self, img):
        self.logReadingImage(img)    
        return self.imageReader.read(self.sourceFolder,img)
    
    def logReadingImage(self, img):
        if self.logger is not None:
            self.logger.log("Reading file %s" % img)
