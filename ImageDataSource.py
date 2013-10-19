class ImageDataSource:
    def __init__(self, fileSystem, imageReader, sourceFolder):
        self.fileSystem = fileSystem
        self.imageReader = imageReader
        self.sourceFolder = sourceFolder
    
    def load(self):
        images = [self.imageReader.read(self.sourceFolder,img) 
                  for img in self.fileSystem.listDir(self.sourceFolder)
                  if self.fileSystem.isFile(self.fileSystem.joinPath(self.sourceFolder,img))]
        return images
