from .fileUtility import FileUtilityBase
from .fileHandlerBase import FileConverter, FileCreator
import os

from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.objects.log.exporter.xes import factory as xes_exporter
from pm4py.objects.log.importer.csv import factory as csv_importer
from pm4py.objects.conversion.log import factory as conversion_factory #error msg
from pm4py.objects.log.util import sorting

# provides file import and export for .xes and .csv files
class FileUtility(FileUtilityBase):
    """
    provides file import and export for XES and csv files
    """
    def __init__(self, defaultDirectory):
        super(FileUtility, self).__init__(defaultDirectory)
        self.registerImport('.xes', XESFileConverter())
        self.registerImport('.csv', CSVFileConverter())
        self.registerExport('.xes', XESFileCreator())

# provides .xes to event log conversion using pm4py
class XESFileConverter(FileConverter):
    """
    provides XES to event log conversion using pm4py
    """
    def __init__(self):
        self._fileType = '.xes'

    def convert(self, filePath):
        """
        function that converts xes files into event logs

        :param filePath: the path to the file
        :return: event log
        """
        return xes_importer.apply(filePath)

# provides .csv to event log converstion using pm4py
class CSVFileConverter(FileConverter):
    """
    provides csv to event log conversion using pm4py
    """
    def __init__(self):
        self._fileType = '.csv'

    def convert(self, filePath):
        """
        function that converts csv files into event logs

        :param filePath: the path to the file
        :return: event log
        """
        csvEventStream = csv_importer.import_event_stream(filePath)
        return conversion_factory.apply(csvEventStream)

# provides event log to .xes file creation using pm4py
class XESFileCreator(FileCreator):
    """
    provides creation of XES files from event logs using pm4py
    """

    def __init__(self):
        super(XESFileCreator, self).__init__()
        self._fileType = '.xes'

    def createFile(self, eventLog, fileName = "", filePath = ""):
        """
        function that creates an XES file from an event log

        :param eventLog: given event log
        :param fileName: name of the file that will be created
        :param filePath: path where the created file should be stored
        :return: path of the stored converted XES file
        """
        destinationPath = self.getDestinationPath()
        if filePath != "":
            destinationPath = filePath
        destinationPath = os.path.join(fileName, filePath)
        xes_exporter.export_log(eventLog, destinationPath)
        return destinationPath
        
        