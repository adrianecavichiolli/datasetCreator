import unittest
import random
import os
import numpy
import cPickle
import cv2
import shutil
from TestUtils import *
from DatasetCreatorFactory import *
from ImageDataSourceFactory import ImageDataSourceFactory
from ConvnetBatchCreatorFactory import ConvnetBatchCreatorFactory

class TestDatasetCreator(unittest.TestCase):

    def test_splitImagesIntoTrainValidAndTest(self):
        self.initialize(folder = 'sample15images')
        
        expectedDistribution = [0.6, 0.2, 0.2]

        imageSource = ImageDataSourceFactory.Create(sourceFolder = self.imgfolder)
        
        datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)
        convnetBatchCreator = ConvnetBatchCreatorFactory.Create()
        
        dataset = datasetCreator.buildDataset(classes = [0,1], datasetSplitIn = expectedDistribution)
        
        convnetBatchCreator.buildBatches(dataset = dataset, 
                                         classes = [0,1], 
                                         classNames = self.classNames,  
                                         saveFolder = os.path.join(self.savefolder, self.datasetName))

                
        self.unionOfBatchesContainAllImages()
        self.assertNumberOfBatches(3)
        self.batchesIntersectionsAreEmpty()
        self.batchesAreSplitAccordingTo(expectedDistribution)
        self.metadataReflectsBatchData()
        
        #self.cleanup()
    
    def folderWasCreated(self):
        assert os.path.exists(os.path.join(self.savefolder, self.datasetName))

    def unionOfBatchesContainAllImages(self):
        batches = self.joinNumpyArray(self.getBatchesData())
        images = self.joinNumpyArray(self.getImagesAsNumpyArray())
        assert numpy.all(numpy.sort(batches, axis=0) == numpy.sort(images, axis = 0))

    def metadataReflectsBatchData(self):
        batchMeta = self.getBatchMeta()
        batchesData = self.getBatchesData()
        batches = self.joinNumpyArray([batchesData[0], batchesData[1]])
        mean = self.CalculateMean(batches)
        
        self.assertEqual(arrayEqualsTo(mean), batchMeta['data_mean'])
        self.assertTrue(batchMeta['data_in_rows'])
        self.assertEqual(batches.shape[1], batchMeta['num_vis'])
        self.assertEqual(self.classNames, batchMeta['label_names'])

    def batchesIntersectionsAreEmpty(self):
        batches = self.getBatchesData()
        for i in range(len(batches)):
            for j in range(i+1, len(batches)):
                self.assertBatchesDontIntersect(batches[i], batches[j])

    def classesAreBalancedWithinBatches(self):
        batches = self.getBatches()
        baseline = numpy.bincount(numpy.array(batches[0]['labels']))*1.0 / len(batches[0]['labels'])
        for batch in batches:
            current = numpy.bincount(numpy.array(batch['labels']))*1.0 / len(batch['labels'])
            numpy.testing.assert_array_almost_equal(current, baseline, decimal=2)
            
    def batchesAreSplitAccordingTo(self, expectedDistribution):
        batches = self.getBatchesData()
        actual = [batches[i].shape[0] for i in range(3)]
        actual = numpy.array(actual)*1.0 / sum(actual)
        numpy.testing.assert_array_almost_equal(actual, numpy.array(expectedDistribution))
    
    def assertNumberOfBatches(self, number):
        self.assertEqual(3, len(self.getBatches()), 'Should have created %d batches' % number)
    
    def assertBatchesDontIntersect(self, batch1, batch2):
        interssection = [x for x in set(tuple(x) for x in batch1) & set(tuple(x) for x in batch2)]
        self.assertEqual(0, len(interssection), 'Batches should not have common elements')

    def joinNumpyArray(self, listOfArrays):
        return numpy.concatenate(listOfArrays)

    def getBatchMeta(self):
        return self.unPickle(os.path.join(self.savefolder, self.datasetName, 'batches.meta'))

    def getBatchesData(self):
        return [batch['data'].T for batch in self.getBatches()]

        
    def getBatches(self):
        files = os.listdir(os.path.join(self.savefolder, self.datasetName))
        batchFiles = [f for f in files if f.startswith('data_batch')]
        batchFiles.sort()

        return [self.unPickle(os.path.join(self.savefolder, self.datasetName, f)) for f in batchFiles]

    def CalculateMean(self, batches):
        total = numpy.sum(batches, axis=0)

        return ((total*1.0) / batches.shape[0]).reshape(-1,1)

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

    def initialize(self, folder):
        self.imgfolder = os.path.join('testdata/',folder)
        self.datasetName = 'result'
        self.savefolder = self.imgfolder
        self.classNames = ['class ' + str(i) for i in range(50)]
                
    def cleanup(self):
        if (len(self.savefolder) > 0 and len(self.datasetName) > 0):
            shutil.rmtree(os.path.join(self.savefolder, self.datasetName))

        
if __name__ == '__main__':
    unittest.main()
