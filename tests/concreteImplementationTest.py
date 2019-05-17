import unittest
from refiningEventLabels.eventLogConverter import FileConverter
from refiningEventLabels.eventLogConverter import FileConverterFactory, FileCreatorFactory

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

        
class DummyXesConverter(FileConverter):
    def __init__(self, type):
        self._fileType = type

    def convert(self, filePath):
        raise NotImplementedError()
