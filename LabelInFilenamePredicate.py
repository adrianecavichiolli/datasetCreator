class LabelInFilenamePredicate:
    def __init__(self, acceptedClasses):
        self.acceptedClasses = acceptedClasses
    
    def __call__(self, img):
        try:
            return int(img[0:2])-1 in self.acceptedClasses
        except:
            return False