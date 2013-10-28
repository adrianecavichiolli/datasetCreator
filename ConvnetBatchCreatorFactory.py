from ConvnetBatchCreator import ConvnetBatchCreator
from BatchBuilder import BatchBuilder
from SingleBatchBuilder import SingleBatchBuilder
from MetaBatchBuilder import MetaBatchBuilder
from BatchRepository import BatchRepository
from Filesystem import FileSystem
from cPickleSerializer import cPickleSerializer

class ConvnetBatchCreatorFactory:
    @staticmethod
    def Create(nTrainingBatches = 1):
        return ConvnetBatchCreator(BatchBuilder(SingleBatchBuilder(), 
                                                MetaBatchBuilder(), 
                                                nTrainingBatches),
                                   BatchRepository(FileSystem(), 
                                                   cPickleSerializer()))
