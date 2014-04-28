from ConvnetDataset import *

def getBrodatzClasses():
    return ['bark', 'beachsand', 'beans', 'burlap', 'd10', 'd11', 'd4', 'd5', 'd51',
 'd52', 'd6', 'd95', 'fieldstone', 'grass', 'ice', 'image09', 'image15', 'image17',
 'image19', 'paper', 'peb54', 'pigskin', 'pressedcl', 'raffia', 'raffia2',
 'reptile', 'ricepaper', 'seafan', 'straw2', 'tree', 'water', 'woodgrain']


def createDatasetBrodatz():
    sourceFolder = '/home/especial/vri/databases/brodatz/as_png'
    saveFolder = '/home/ppginf/lghafemann/nobackup/data/brodatz' 
    expectedDistribution = [0.3, 0.2, 0.5]

    classNames = getBrodatzClasses()
    classNumbers = range(len(classNames))

    ConvnetDataset.CreateConvNetDataset(SourceFolder = sourceFolder, 
                                            TargetFolder = saveFolder,
                                            ExpectedDistribution = expectedDistribution,
                                            GetLabelsFrom = LabelFromList(classNames),
                                            Classes = classNumbers,
                                            ClassNames = classNames,
                                            SplitFunction = GroupingSplit(),
                                            Grayscale = True)

if __name__ == '__main__':
    createDatasetBrodatz()

