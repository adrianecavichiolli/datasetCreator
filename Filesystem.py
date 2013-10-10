import os

class FileSystem:
	def makeDir(self, fullPath):
		if (not os.path.exists(fullPath)):
			return os.mkdir(fullPath)
	
	def joinPath(self, path1, path2):
		return os.path.join(path1,path2)
	
	def listDir(self, path):
		return os.listdir(path)

	def isFile(self, path):
		return os.path.isfile(path)