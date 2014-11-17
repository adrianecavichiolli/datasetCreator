from ConvnetDataset import *

def createDataset():
    sourceFolder = '/home/especial/vri/databases/florestais/florestais-micro'
    saveFolder  = '/home/especial/vri/databases/preprocessados/micro_100pct'
    expectedDistribution = [0.5, 0.2, 0.3]

    dataset = ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            Classes = range(112), 
                                            ClassNames = range(112),  
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            NumTrainBatches = 1,
                                            Grayscale = True)
def createDataset_Xpct(pct, fold):
    sourceFolder = '/home/especial/vri/databases/florestais/florestais-micro'
    saveFolder  = '/home/especial/vri/databases/preprocessados/micro_%dpct_fold%d' % (pct, fold)
    print "saving to %s" % saveFolder
    expectedDistribution = [0.5, 0.2, 0.3]

    dataset = ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            ResizeBy = ResizeByPercent((pct*1.0)/100.0),
                                            Classes = range(112), 
                                            ClassNames = range(112),  
                                            GetLabelsFrom = LabelFromFirstChars(3),
                                            NumTrainBatches = 1,
                                            Grayscale = True)

if __name__ == '__main__':
    createDataset_Xpct(30,2)
    createDataset_Xpct(30,3)
    #createDataset_Xpct(50)
    #createDataset_Xpct(70)
    #createDataset()
