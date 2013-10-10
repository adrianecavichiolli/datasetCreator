import numpy

class arrayEqualsTo:
    def __init__(self, array):
        self.array = array
    def __eq__(self, otherarray):
        return numpy.alltrue(self.array == otherarray)
    def __str__(self):
        return self.array.__str__()
    def __repr__(self):
        return self.array.__repr__()
    
