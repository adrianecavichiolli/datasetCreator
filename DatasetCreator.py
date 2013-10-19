class DatasetCreator:
	def __init__(self, fileSystem, imageReader, batchBuilder, batchRepository, imageFolder, saveFolder, classNames):
		self.imageFolder = imageFolder
		self.baseSaveFolder = saveFolder
		self.fileSystem = fileSystem
		self.imageReader = imageReader
		self.batchBuilder = batchBuilder
		self.batchRepository = batchRepository
		self.classNames = classNames

	def CreateConvNet(self, name, classes, datasetSplitIn = [0.6, 0.2, 0.2]):
		self.saveFolder = self.fileSystem.joinPath(self.baseSaveFolder, name)
		self.fileSystem.makeDir(self.saveFolder)
		
		images = [self.imageReader.read(self.imageFolder,img) 
				  for img in self.fileSystem.listDir(self.imageFolder)
				  if self.fileSystem.isFile(self.fileSystem.joinPath(self.imageFolder,img))]

		batches = self.batchBuilder.build(images, classes, self.classNames, datasetSplitIn)
		self.batchRepository.save(batches, self.saveFolder)