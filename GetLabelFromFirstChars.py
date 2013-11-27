class GetLabelFromFirstChars:
    def __init__(self, nChars):
        self.nChars = nChars
    
    def __call__(self, filename):
        return int(filename[0:self.nChars]) -1