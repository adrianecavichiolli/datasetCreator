
class FixedDatasetSplitter:
    def __init__(self, filenames_in_train, filenames_in_valid, filenames_in_test):
        self.filenames_in_train = filenames_in_train
        self.filenames_in_valid = filenames_in_valid
        self.filenames_in_test = filenames_in_test

    def split(self, dataset, expectedDistribution_ignored):
        items = {item.getFilename(): item for item in dataset}

        train = [items[filename] for filename in self.filenames_in_train]
        valid = [items[filename] for filename in self.filenames_in_valid]
        test = [items[filename] for filename in self.filenames_in_test]

        return train, valid, test