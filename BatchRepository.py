class BatchRepository:
	def __init__(self, fileSystem, serializer):
		self.fileSystem = fileSystem
		self.serializer = serializer
	
	def save(self, batches, saveFolder):
		if (not self.fileSystem.pathExists(saveFolder)):
			self.fileSystem.makeDir(saveFolder)
		for name, data in batches.iteritems():
			filename = self.fileSystem.joinPath(saveFolder, name)
			self.serializer.write(filename, data) 