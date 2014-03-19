import unittest
from FileGroupingDatasetSplitter import FileGroupingDatasetSplitter
import numpy
from mock import Mock
import itertools


class testFileGroupingDatasetSplitter(unittest.TestCase):

    def test_SplitsImages(self):
        items = [imageNamed(0,"001_01.bmp"), imageNamed(0,"001_03.bmp"), imageNamed(0,"001_02.bmp")]

        target = FileGroupingDatasetSplitter(1)
        result = target.split(items, [.6, .2, .2])

        self.assertEquals(sorted(self.joinLists(result)), sorted(items))
        for d in result:
            self.assertEquals(1, len(d))

    def test_AllImagesFromSampeSampleAreGrouped(self):
        itemlist = []
        for sampleID in ["001", "015", "230"]:
            itemlist.append([imageNamed(int(sampleID)-1, "%s_%d.png" % (sampleID, (i)+1)) for i in range(27)])

        items = self.joinLists(itemlist)
        numpy.random.shuffle(items)
        
        target = FileGroupingDatasetSplitter(9)
        result = target.split(items, [.6,.2,.2])

        print sorted([img.getFilename() for img in result[0] if img.getFilename()[0:3] == "001"])
        print sorted([img.getFilename() for img in result[1] if img.getFilename()[0:3] == "001"])
        print sorted([img.getFilename() for img in result[2] if img.getFilename()[0:3] == "001"])

        totalAfterSplit = self.joinLists(result)
        
        self.assertEqual(sorted(totalAfterSplit), sorted(items))
        
        for sampleID in ["001", "015", "230"]:
            self.assertSamplesAreInOnlyOneSet(["%s_%d.png" % (sampleID, i) for i in range(1, 10)], result)
            self.assertSamplesAreInOnlyOneSet(["%s_%d.png" % (sampleID, i) for i in range(10, 19)], result)
            self.assertSamplesAreInOnlyOneSet(["%s_%d.png" % (sampleID, i) for i in range(19, 28)], result)
    
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


