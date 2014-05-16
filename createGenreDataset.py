
from ConvnetDataset import *

def SplitGenreDataset(dataset, numRows, numCols):
    original_image_size = dataset[0][0].getShape()
    numPatches = numRows * numCols
    rowSize = original_image_size[0] / numRows
    colSize = original_image_size[1] / numCols

    allDatasets = []
    for set in dataset:
        thisSet = [list() for i in xrange(numPatches)]
        for image in set:
            for i in xrange(numRows):
                for j in xrange(numCols):
                    patchIndex = i * numCols + j
                    imagePatch = image.image[i * rowSize: (i+1) * rowSize, 
                                             j * colSize: (j+1) * colSize]
                    newImage = image.createCopyWithImage(imagePatch)
                    thisSet[patchIndex].append(newImage)
        allDatasets.append(thisSet)
    return allDatasets

def createDatasetGenre_point6():
    sourceFolder = '/home/especial/vri/databases/generos_musicais/classinname'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/Genre_first_part'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(10)
    classNumbers = range(10)

    dataset = ConvnetDataset.CreateDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent(0.6),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            Grayscale = True)
    datasets = SplitGenreDataset(dataset, 10, 3)

    mydata = (datasets[0][0], datasets[1][0], datasets[2][0])
    convnetBatchCreator.buildBatches(dataset = mydata, 
                                     classes = classNumbers,
                                     classNames = classNames,
                                     saveFolder = saveFolder)
        

if __name__ == '__main__':
    createDatasetGenre_point6()

