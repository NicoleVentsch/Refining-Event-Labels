import unittest
import os
import glob
import time

from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig

class TestFileConverterFactory(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestFileConverterFactory, self).__init__(*args, **kwargs)
        currentDir = os.path.dirname(__file__)
        self.__testFiles = os.path.join(currentDir, 'TestFiles', 'FileStore')
        self._maxNumberOfFiles = 5
        self._deleteFilesInDir()

    def testIfFileStoreKeepsTrackOfTooManyFiles(self):
        self._createRequiredFiles(8, "test", "txt")
        fileStore = self._createFileStore(self._maxNumberOfFiles)
        createdFiles = [name for name in os.listdir(self.__testFiles) if os.path.isfile(os.path.join(self.__testFiles, name))]
        numberFiles = len(createdFiles)
        self.assertEqual(self._maxNumberOfFiles, numberFiles)
        for i in range(self._maxNumberOfFiles):
            self.assertTrue("test" + str(i) + ".txt" in createdFiles, "test" + str(i) + ".txt should be in test dir")
        for i in range(self._maxNumberOfFiles + 1, 8):
            self.assertTrue("test" + str(i) + ".txt" not in createdFiles, "test" + str(i) + ".txt should not be in test dir")

        self._deleteFilesInDir()

        self._createRequiredFiles(self._maxNumberOfFiles - 2, "test", "xml")
        fileStore = self._createFileStore(self._maxNumberOfFiles)
        numberFiles = len([name for name in os.listdir(self.__testFiles) if os.path.isfile(os.path.join(self.__testFiles, name))])
        self.assertEqual(self._maxNumberOfFiles - 2, numberFiles)

    def testFileSavingInDestinationDir(self):
        tmpFolder = os.path.join(os.path.dirname(__file__), "TestFiles")
        fileStore = self._createFileStore(self._maxNumberOfFiles)
        self._createRequiredFiles(7, "test", "csv", tmpFolder)
        createdFiles = [name for name in os.listdir(tmpFolder) if os.path.isfile(os.path.join(tmpFolder, name))]
        createdFiles.sort(reverse = True)
        for file in createdFiles:
            fileStore.storeFile(os.path.join(tmpFolder,file))
        
        createdFilesTmpFolder = [name for name in os.listdir(tmpFolder) if os.path.isfile(os.path.join(tmpFolder, name))]
        self.assertEqual(0, len(createdFilesTmpFolder))

        for i in range(self._maxNumberOfFiles):
            shouldFilePath = os.path.join(self.__testFiles, "test" + str(i) + ".csv")
            self.assertTrue(os.path.isfile(shouldFilePath), "File " + shouldFilePath + " should exist")
        for i in range(self._maxNumberOfFiles + 1, 7):
            shouldNotFilePath = os.path.join(self.__testFiles, "test" + str(i) + ".csv")
            self.assertFalse(os.path.isfile(shouldNotFilePath), "File " + shouldFilePath + "  should not exist")

        self._deleteFilesInDir()

    def _deleteFilesInDir(self):
        files = glob.glob(os.path.join(self.__testFiles, '*'))
        for f in files:
            os.remove(f)

    def _createRequiredFiles(self, number, name, fileType, path = ""):
        if path == "":
            path = self.__testFiles
        for i in range(number):
           open(os.path.join(path, name + str(i) + "." + fileType), "a").close()
           time.sleep(0.05)

    def _createFileStore(self, numberFiles):
        config = FileStoreConfig.CreateWithMaxNumberFilesAndFilesTypes(self.__testFiles, numberFiles, ["txt", "xml", "csv"])
        return FileStore(config)
