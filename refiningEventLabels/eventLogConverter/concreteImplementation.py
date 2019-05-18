from .fileUtility import FileUtilityBase
from .fileHandlerBase import FileConverter
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.objects.log.importer.csv import factory as csv_importer
from pm4py.objects.conversion.log import factory as conversion_factory
from pm4py.objects.log.util import sorting

class FileUtility(FileUtilityBase):

    def __init__(self, defaultDirectory):
        super(FileUtility, self).__init__(defaultDirectory)
        self.registerImport('.xes', XESFileConverter())
        self.registerImport('.csv', CSVFileConverter())

class XESFileConverter(FileConverter):
    def __init__(self):
        self._fileType = '.xes'

    def convert(self, filePath):
        return xes_importer.apply(filePath)

class CSVFileConverter(FileConverter):
    def __init__(self):
        self._fileType = '.csv'

    def convert(self, filePath):
        csvEventStream = csv_importer.import_event_stream(filePath)
        return conversion_factory.apply(csvEventStream)
        