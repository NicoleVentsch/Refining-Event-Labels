import unittest
import os
import glob
from refiningEventLabels.lib.eventLogConverter import FileConverter
from refiningEventLabels.lib.eventLogConverter import FileConverterFactory, FileCreatorFactory
from refiningEventLabels.lib.eventLogConverter import FileUtility
from refiningEventLabels.lib.eventLogConverter import XESFileCreator
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
        xesPath = os.path.join(dirname, 'Ressources/example.xes')

        fileCreator = FileUtility(rootDir)
        eventLog = fileCreator.getEventLogFromFile(xesPath)
        eventLog = sorting.sort_timestamp(eventLog)
        self.assertEqual(len(eventLog), 6)

    def testCSVConversion(self):
        dirname = os.path.dirname(__file__)
        rootDir = os.path.join(dirname, 'TestFiles')
        csvPath = os.path.join(dirname, 'Ressources/example.csv')

        fileCreator = FileUtility(rootDir)
        eventLog = fileCreator.getEventLogFromFile(csvPath)
        eventLog = sorting.sort_timestamp(eventLog)
        self.assertEqual(len(eventLog), 6)

# Tests if FileCreators can create a file with the correct path and extension. 
# The file structure is not checked, because it is set by the creator
# To test multiple FileCreator register the creator with the registerFileCreator function
class FileCreatorTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(FileCreatorTest, self).__init__(*args, **kwargs)
        self._fileCreator = set()
        self.registerFileCreator('xes', XESFileCreator())

    def registerFileCreator(self, type, instance):
        self._fileCreator.add((type, instance))

    def getFileCreators(self):
        return self._fileCreator

    def testFileCreator(self):
        self._deletingTestFiles()
        fileCreators = self.getFileCreators()
        dirname = os.path.dirname(__file__)
        xesPath = os.path.join(dirname, 'Ressources/example.xes')
        destinationPath = os.path.join(dirname, 'TestFiles' )
        fileCreator = FileUtility(xesPath)
        eventLog = fileCreator.getEventLogFromFile(xesPath)
        for creatorInfo in fileCreators: 
            creatorInfo[1].createFile(eventLog, "testFile." + creatorInfo[0], destinationPath)
        
        for creatorInfo in fileCreators:
            shouldCreatedFile = os.path.join(destinationPath, "testFile." + creatorInfo[0])
            self.assertTrue(os.path.isfile(shouldCreatedFile))
       
        
        
    def _deletingTestFiles(self):
        dirname = os.path.dirname(__file__)
        destinationPath = os.path.join(dirname, 'TestFiles')
        files = glob.glob(os.path.join(destinationPath, '*'))
        for f in files:
            os.remove(f)
                

        
class DummyXesConverter(FileConverter):
    def __init__(self, type):
        self._fileType = type

    def convert(self, filePath):
        raise NotImplementedError()