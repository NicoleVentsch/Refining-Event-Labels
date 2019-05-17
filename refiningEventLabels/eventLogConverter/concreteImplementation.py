from fileUtility import FileUtilityBase
from fileHandlerBase import FileConverter
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.objects.log.importer.csv import factory as csv_importer

class FileUtility(FileUtilityBase):

    def __init__(self, defaultDirectory):
        super(FileUtility, self).__init__(defaultDirectory)
        self.registerImport('.xes', XESFileConverter())
        self.registerImport('.csv', CSVFileConverter())

class XESFileConverter(FileConverter):
    def __init__(self):
        self._fileType = '.xes'

    def convert(self, filePath):
        return xes_importer.import_log(filePath)

class CSVFileConverter(FileConverter):
    def __init__(self):
        self._fileType = '.csv'

    def convert(self, filePath):
        return csv_importer.import_event_log(filePath)
        