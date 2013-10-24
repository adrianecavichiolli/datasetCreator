import numpy

class MetaBatchBuilder:
    
    def build(self, dataset, classNames):
        meta = {}
        train = dataset[0]
        valid = dataset[1]
        numImgPixels = train[0].getArray().shape[0]
        meta['num_vis'] = numImgPixels
        meta['data_mean'] = self.calculateMean(train + valid, numImgPixels).reshape(-1,1)
        meta['data_in_rows'] = True
        meta['label_names'] = classNames
        return meta
    
    def calculateMean(self, imgList, imgSize):
        total = numpy.zeros(imgSize)
        for img in imgList:
            total += img.getArray()
        return total / len(imgList)
