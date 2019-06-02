import unittest
import os
import json
import glob
from flask import Flask, request

from refiningEventLabels.api.fileUpload import FileUpload
from refiningEventLabels.lib.fileStore import FileStoreConfig


app = Flask(__name__)
app.app_context()

class FileUploadAPITest(unittest.TestCase):

    def __fakeGETRequest(self):
        return FakeRequest("GET")

    def __fakePOSTRequest(self):
         return FakeRequest("POST")

    def __createFileUploadPage(self):
        dirname = os.path.dirname(__file__)
        dirname = os.path.join(dirname, 'TestFiles', 'FileUpload', 'Upload')
        config = FileStoreConfig(dirname, 5, ["xes", "csv"])
        return FileUpload(config)

    def testGetRequest(self):
        request = self.__fakeGETRequest()
        fileUploadPage = self.__createFileUploadPage()
        resultJson = fileUploadPage.execute(request)

        shouldFileInformation = self.__getExpectedFilesInfos()
        expectedJson = json.dumps(shouldFileInformation)
        self.assertEqual(expectedJson, resultJson)

    def __getExpectedFilesInfos(self):
        shouldFileInformation = []
        currentDir = os.path.dirname(__file__)
        fileUploadDir = os.path.join(currentDir, 'TestFiles', 'FileUpload', 'Upload')

        files = os.listdir(fileUploadDir)
        files = [f for f in files]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(fileUploadDir, x)))
        for file in files:
            fulleFilePath = os.path.join(fileUploadDir, file)
            shouldFileInformation.append({"name": file, "tstamp": os.path.getmtime(fulleFilePath) })
        return shouldFileInformation
    
    def testPostRequest(self):
        request = self.__fakePOSTRequest()
        fileUploadPage = self.__createFileUploadPage()
        result = fileUploadPage.execute(request)

        currentDir = os.path.dirname(__file__)
        fileUploadDir = os.path.join(currentDir, 'TestFiles', 'FileUpload', 'Upload')
        fileBeforeUploadDir = os.path.join(currentDir, 'TestFiles', 'FileUpload', 'ExampleUploadFile')

        self.assertTrue(os.path.isfile(os.path.join(fileUploadDir, "example5.xes")))
        self.assertFalse(os.path.isfile(os.path.join(fileBeforeUploadDir, "example5.xes")))
        self.assertEqual("File Uploaded", result)

        os.rename(os.path.join(fileUploadDir, "example5.xes"), os.path.join(fileBeforeUploadDir, "example5.xes"))


class FakeRequest():

    def __init__(self, requestType):
        self._type = requestType
        currentDir = os.path.dirname(__file__)
        fileUploadDir = os.path.join(currentDir, 'TestFiles', 'FileUpload', 'ExampleUploadFile', "example5.xes")
        self._files = { "eventLog": FileInfo(fileUploadDir)} 

    @property
    def method(self):
        return self._type

    @property
    def files(self):
        return self._files

class FileInfo():
    def __init__(self, filename):
        self.filename = filename
