class DatasetGridExtractor:
    def __init__ (self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols

    def run(self, dataset):
        original_image_size = dataset[0][0].getShape()
        numPatches = self.numRows * self.numCols
        rowSize = original_image_size[0] / self.numRows
        colSize = original_image_size[1] / self.numCols

        allDatasets = []
        for set in dataset:
            thisSet = [list() for i in xrange(numPatches)]
            for image in set:
                for i in xrange(self.numRows):
                    for j in xrange(self.numCols):
                        patchIndex = i * self.numCols + j
                        imagePatch = image.image[i * rowSize: (i+1) * rowSize, 
                                                 j * colSize: (j+1) * colSize]
                        newImage = image.createCopyWithImage(imagePatch)
                        thisSet[patchIndex].append(newImage)
            allDatasets.append(thisSet)
        return allDatasets
