import numpy

class SingleBatchBuilder:
    
    def build(self, listOfImages, classes):
        classMapping = {classes[i]:i for i in range(len(classes))}
        batch = {}
        data = [img.getArray().T for img in listOfImages]
        batch['data']= numpy.asarray(data).T
        batch['labels'] = [classMapping[img.getLabel()] for img in listOfImages]
        batch['filenames'] = [img.getFilename() for img in listOfImages]
        return batch
