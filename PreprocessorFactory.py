from ExtractGridPatches import ExtractGridPatches
class PreprocessorFactory:
    @staticmethod
    def CreateExtractGridPatches(patchSize):
        return ExtractGridPatches(patchSize)