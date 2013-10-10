import cPickle

class cPickleSerializer:
    def write(self, filename, data):
        cPickle.dump(data, open(filename,'wb'))