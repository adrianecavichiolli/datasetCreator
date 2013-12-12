class LabelInFilenamePredicate:
    def __init__(self, getLabelFunction, acceptedClasses):
        self.acceptedClasses = acceptedClasses
        self.getLabelFunction = getLabelFunction
    
    def __call__(self, img):
        try:
            return self.getLabelFunction(img) in self.acceptedClasses
        except:
            return False