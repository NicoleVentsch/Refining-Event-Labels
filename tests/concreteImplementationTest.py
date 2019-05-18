import unittest
import os
from refiningEventLabels.eventLogConverter import FileConverter
from refiningEventLabels.eventLogConverter import FileConverterFactory, FileCreatorFactory
from refiningEventLabels.eventLogConverter import FileUtility
from pm4py.objects.log.util import sampling, sorting

class TestFileConverterFactory(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFileConverterFactory, self).__init__(*args, **kwargs)
        self._fileTypes = ['.xes', '.csv', '.xls']

    def _setUpFileConverter(self):
        return FileConverterFactory()

    def _setUpTestData(self):
        fileConverterFactory = self._setUpFileConverter()
        for type in self._fileTypes:
            fileConverterFactory.register(type, DummyXesConverter(type))
        return fileConverterFactory

    def testReturnRightFileConverter(self):
        fileConverterFactory = self._setUpTestData()
        for type in self._fileTypes:
            self.assertEqual(fileConverterFactory.create(type).getFileType(), type)

class FileUtilityTest(unittest.TestCase):

    def testXESConversion(self):
        dirname = os.path.dirname(__file__)
        rootDir = os.path.join(dirname, 'TestFiles')
        xesPath = os.path.join(dirname, 'Ressources/running-example.xes')

        fileCreator = FileUtility(rootDir)
        eventLog = fileCreator.getEventLogFromFile(xesPath)
        eventLog = sorting.sort_timestamp(eventLog)
        self.assertEqual(len(eventLog), 6)

    def testCSVConversion(self):
        dirname = os.path.dirname(__file__)
        rootDir = os.path.join(dirname, 'TestFiles')
        csvPath = os.path.join(dirname, 'Ressources/running-example.csv')

        fileCreator = FileUtility(rootDir)
        eventLog = fileCreator.getEventLogFromFile(csvPath)
        eventLog = sorting.sort_timestamp(eventLog)
        self.assertEqual(len(eventLog), 6)

        
class DummyXesConverter(FileConverter):
    def __init__(self, type):
        self._fileType = type

    def convert(self, filePath):
        raise NotImplementedError()