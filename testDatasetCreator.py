import unittest
import random
import os
import numpy
import cPickle
import cv2
from DatasetCreatorFactory import *

#class TestDatasetCreator(unittest.TestCase):
class TestDatasetCreator():
	def setUp(self):
		self.imgfolder = 'testdata/sample3images'
		self.savefolder = 'testdata/sample3images'
		self.randomNumberGenerator = random.Random(1)
		self.target = DatasetCreatorFactory.create(self.imgfolder, 
												   self.savefolder, 
												   self.randomNumberGenerator)
	def test_1class3images(self):
		self.datasetName = 'result'
		
		self.target.CreateConvNet(classes = [0], name = self.datasetName)
		
		self.folderWasCreated()
		self.unionOfBatchesContainAllImages()
		self.batchesIntersectionsAreEmpty()
	
	def folderWasCreated(self):
		assert os.path.exists(os.path.join(self.savefolder, self.datasetName))
	
	def unionOfBatchesContainAllImages(self):
		batches = self.joinNumpyArray(self.getBatchesData())
		images = self.joinNumpyArray(self.getImagesAsNumpyArray())
		assert numpy.all(numpy.sort(batches, axis=0) == numpy.sort(images, axis = 0))
	
	def batchesIntersectionsAreEmpty(self):
		batches = self.getBatchesData()
		for i in range(len(batches)):
			for j in range(i+1, len(batches)):
				self.assertBatchesDontIntersect(batches[i], batches[j])
	
	def assertBatchesDontIntersect(self, batch1, batch2):
		assert numpy.intersect1d(batch1, batch2).size == 0
		
	def joinNumpyArray(self, listOfArrays):
		return numpy.concatenate(listOfArrays)
	
	def getBatchesData(self):
		return [batch['data'].T for batch in self.getBatches()]
		
	def getBatches(self):
		files = os.listdir(os.path.join(self.savefolder, self.datasetName))
		batchFiles = [f for f in files if f.startswith('data_batch')]
		batchFiles.sort()
		
		return [self.unPickle(os.path.join(self.savefolder, self.datasetName, f)) for f in batchFiles]
		
	def getImagesAsNumpyArray(self):
		imageList = self.getImages()
		return [self.imageToNumpyArray(img) for img in imageList]
	
	def getImages(self):
		files = [f for f in os.listdir(self.imgfolder) 
                 if os.path.splitext(f)[1].lower() == ".jpg"]
		return [cv2.imread(os.path.join(self.imgfolder,f)) for f in files]
	
	def imageToNumpyArray(self, img):
		imgCopy = numpy.copy(img)
		imgCopy[:,:,[0,2]] = imgCopy[:,:,[2,0]]
		return numpy.transpose(imgCopy, (2,0,1)).reshape(1,-1)
		
	def unPickle(self, filename):
		return cPickle.load(open(filename, 'rb'))
		
