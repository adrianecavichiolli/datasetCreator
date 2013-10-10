class DatasetCreator:
	def __init__(self, fileSystem, imageReader, batchBuilder, imageFolder, saveFolder):
		self.imageFolder = imageFolder
		self.baseSaveFolder = saveFolder
		self.fileSystem = fileSystem
		self.imageReader = imageReader
		self.batchBuilder = batchBuilder

	def CreateConvNet(self, name):
		self.saveFolder = self.fileSystem.joinPath(self.baseSaveFolder, name)
		self.fileSystem.makeDir(self.saveFolder)
		
		images = [self.imageReader.read(self.imageFolder,img) 
				  for img in self.fileSystem.listDir(self.imageFolder)
				  if self.fileSystem.isFile(self.fileSystem.joinPath(self.imageFolder,img))]

		self.batchBuilder.build(images, self.saveFolder)