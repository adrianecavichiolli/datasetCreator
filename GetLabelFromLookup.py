class GetLabelFromLookup:
    def __init__(self, classNames, separator):
        self.classMapping = self._BuildDictionary(classNames)
        self.separator = separator
    
    def __call__(self, filename):
        separator_index = filename.find("_")
        if (separator_index == -1):
            raise FilenameDoesNotContainSeparatorError()

        thisClass = filename[0:separator_index]

        if (not self.classMapping.has_key(thisClass)):
            raise FilenameContainsClassNotInLookup("Class not found: %s" % thisClass)

        return self.classMapping[thisClass]

    def _BuildDictionary(self,classNames):
        numclasses = len(classNames)
        return dict(zip(classNames, range(numclasses)))

class FilenameDoesNotContainSeparatorError(Exception):
    pass

class FilenameContainsClassNotInLookup(Exception):
    pass
