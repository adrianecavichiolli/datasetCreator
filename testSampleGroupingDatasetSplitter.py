import unittest
from SampleGroupingDatasetSplitter import SampleGroupingDatasetSplitter
from GetSampleNumberFromFilename import GetSampleNumberFromFilename
import numpy
from mock import Mock
import itertools
import re

class testSampleGroupingDatasetSplitter(unittest.TestCase):  
    def setUp(self):
        self.getNumberFunction = GetSampleNumberFromFilename()

    def test_SplitsImages(self):
        items = [imageNamed(0,"bark_01_o.bmp"), imageNamed(0,"bark_02_o.bmp"), imageNamed(0,"bark_03_o.bmp")]

        target = SampleGroupingDatasetSplitter(self.getNumberFunction)
        result = target.split(items, [.6, .2, .2])

        self.assertEquals(sorted(self.joinLists(result)), sorted(items))
        for d in result:
            self.assertEquals(1, len(d))


    def test_AllImagesFromSampeSampleAreGrouped(self):
        itemlist = []
        samples = [("bark_00", 0), ("bark_01", 0), ("bark_02",0), ("beans_01", 1), ("beans_02",1), ("beans_03",1)]
        for sample in samples:
            sampleID = sample[0]
            sampleClass = sample[1]
            itemlist.append([imageNamed(sampleClass , "%s_%s.png" % (sampleID, imgType)) for imgType in ["o", "r", "rs", "s"]])

        items = self.joinLists(itemlist)
        numpy.random.shuffle(items)
        
        target = SampleGroupingDatasetSplitter(self.getNumberFunction)
        result = target.split(items, [.3,.3,.4])

        totalAfterSplit = self.joinLists(result)
        
        self.assertEqual(sorted(totalAfterSplit), sorted(items))
        
        for sample in samples:
            sampleID = sample[0]
            self.assertSamplesAreInOnlyOneSet(["%s_%s.png" % (sampleID, imgType) for imgType in ["o", "r", "rs", "s"]], result)
    
    def joinLists(self, listOfLists):
        return list(itertools.chain.from_iterable(listOfLists))
    
    def assertSamplesAreInOnlyOneSet(self, samples, dataset):
        firstSample = samples[0]
    
        if firstSample in getFilenames(dataset[0]):
            self.assertAllSamplesAreIn(samples, dataset[0])
            self.assertnoSamplesAreIn(samples, dataset[1])
            self.assertnoSamplesAreIn(samples, dataset[2])
        elif firstSample in getFilenames(dataset[1]):
            self.assertnoSamplesAreIn(samples, dataset[0])
            self.assertAllSamplesAreIn(samples, dataset[1])
            self.assertnoSamplesAreIn(samples, dataset[2])
        else:
            self.assertnoSamplesAreIn(samples, dataset[0])
            self.assertnoSamplesAreIn(samples, dataset[1])
            self.assertAllSamplesAreIn(samples, dataset[2])


    def assertAllSamplesAreIn(self, samples, data):
        for sample in samples:
            self.assertIn(sample, getFilenames(data))
   
    def assertnoSamplesAreIn(self, samples, data):
        for sample in samples:
            self.assertNotIn(sample,getFilenames(data))


def imageNamed(label, name):
    img = Mock()
    img.getLabel.return_value=label
    img.getFilename.return_value = name
    img.__str__ = Mock(return_value = name)
    return img


def getFilenames(data):
    return [img.getFilename() for img in data]

if __name__=='__main__':
    unittest.main()

