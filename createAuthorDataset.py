from ConvnetDataset import *

def createDatasetBFL_256_inv():
    sourceFolder = '/home/especial/vri/databases/autoria/BFL'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/BFL_64_inv_split'
    expectedDistribution = [0.5, 0.2, 0.3]

    classNames = range(315)
    classNumbers = range(315)

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = FileGroupingSplit(numFilePerImage = 9),
                                            Grayscale = True)

def createDatasetIAM():
    sourceFolder = '/home/especial/vri/databases/autoria/IAM'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/IAM_orig'
    expectedDistribution = [0.5, 0.2, 0.3]

    getLabelFunction = GetLabelFromFirstChars(nChars=3)
    imageReader = GrayscaleOpenCVImgReader(imageFactory = LabeledImageFactory(getLabelFunction, True),
                           openCV = cv2, 
                           fileSystem = FileSystem())

    invertingImageReader = ImageReaderDecorator(imageReader =  imageReader,
                                   decorator = ImageInverter())

    imageSource = ImageDataSourceFactory.CreateWithImageReader(
                      imageReader = invertingImageReader,
                      sourceFolder = sourceFolder,
                      log=True, 
                      getLabelFunction = getLabelFunction)

    datasetCreator = DatasetCreatorFactory.Create(imageSource = imageSource)

    dataset = datasetCreator.buildDataset(datasetSplitIn = expectedDistribution)
    convnetBatchCreator = ConvnetBatchCreatorFactory.Create(nTrainingBatches = 3)
        
    convnetBatchCreator.buildBatches(dataset = dataset, 
                                     classes = range(672), 
                                     classNames = range(672),  
                                     saveFolder = saveFolder)

if __name__ == '__main__':
    createDatasetBFL_256_inv()
    #createDatasetIAM()
