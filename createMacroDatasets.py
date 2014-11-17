from ConvnetDataset import *

def createDataset():
    sourceFolder = '/home/especial/vri/databases/florestais/florestais-macro'
    saveFolder  = '/home/especial/vri/databases/preprocessados/macro_100pct'
    expectedDistribution = [0.35, 0.15, 0.5]

    dataset = ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            Classes = range(41),
                                            ClassNames = range(41),
                                            NumTrainBatches = 1)
def createDataset_Xpct(pct, fold):
    sourceFolder = '/home/especial/vri/databases/florestais/florestais-macro'
    saveFolder  = '/home/especial/vri/databases/preprocessados/macro_%dpct_fold%d' % (pct, fold)
    print "saving to: %s" % saveFolder
    expectedDistribution = [0.35, 0.15, 0.5]

    dataset = ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent((pct*1.0)/100.0),
                                            Classes = range(41),
                                            ClassNames = range(41),
                                            NumTrainBatches = 1)

def createDataset_Xpct_grayscale(pct, fold):
    sourceFolder = '/home/especial/vri/databases/florestais/florestais-macro'
    saveFolder  = '/home/especial/vri/databases/preprocessados/macro_grayscale_%dpct_fold%d' % (pct, fold)
    print "saving to: %s" % saveFolder
    expectedDistribution = [0.35, 0.15, 0.5]

    dataset = ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent((pct*1.0)/100.0),
                                            Classes = range(41),
                                            ClassNames = range(41),
                                            NumTrainBatches = 1,
                                            Grayscale = True)
if __name__ == '__main__':
    createDataset_Xpct_grayscale(10,1)
    #createDataset_Xpct(10, 2)
    #createDataset_Xpct(10, 3)
#    createDataset_Xpct(50)
#    createDataset()
