class ImageDataSource:
    def __init__(self, fileSystem, imageReader, sourceFolder):
        self.fileSystem = fileSystem
        self.imageReader = imageReader
        self.sourceFolder = sourceFolder
        self.logger = None
        self.shouldLoadImage = lambda x:True
    
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

    def setLogger(self, logger):
        self.logger = logger
    
    def setFilenamePredicate(self, predicate):
        self.shouldLoadImage = predicate
