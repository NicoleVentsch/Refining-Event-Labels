import unittest
import os
import glob

from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig

class TestFileConverterFactory(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFileConverterFactory, self).__init__(*args, **kwargs)
        currentDir = os.path.dirname(__file__)
        self.__testFiles = os.path.join(currentDir, 'TestFiles', 'FileStore')
        self._deleteFilesInDir()

    def testIfFileStoreKeepsTrackOfTooManyFiles(self):
        maxNumberOfFiles = 5
        self._createRequiredFiles(8, "test", "txt")
        fileStore = self._createFileStore(maxNumberOfFiles)
        numberFiles = len([name for name in os.listdir(self.__testFiles) if os.path.isfile(os.path.join(self.__testFiles, name))])
        self.assertEqual(maxNumberOfFiles, numberFiles)

        self._deleteFilesInDir()

        self._createRequiredFiles(maxNumberOfFiles - 2, "test", "xml")
        fileStore = self._createFileStore(maxNumberOfFiles)
        numberFiles = len([name for name in os.listdir(self.__testFiles) if os.path.isfile(os.path.join(self.__testFiles, name))])
        self.assertEquals(maxNumberOfFiles - 2, numberFiles)



        

    def _deleteFilesInDir(self):
        files = glob.glob(os.path.join(self.__testFiles, '*'))
        for f in files:
            os.remove(f)

    def _createRequiredFiles(self, number, name, fileType):
        for i in range(number):
           open(os.path.join(self.__testFiles, name + str(i) + "." + fileType), "a").close()

    def _createFileStore(self, numberFiles):
        config = FileStoreConfig.CreateWithMaxNumberFilesAndFilesTypes(self.__testFiles, numberFiles, ["txt", "xml", "csv"])
        return FileStore(config)
