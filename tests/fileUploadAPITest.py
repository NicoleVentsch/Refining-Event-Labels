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

    def __createFileUploadPage(self):
        dirname = os.path.dirname(__file__)
        dirname = os.path.join(dirname, 'TestFiles', 'FileUpload')
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
        fileUploadDir = os.path.join(currentDir, 'TestFiles', 'FileUpload')

        files = os.listdir(fileUploadDir)
        files = [f for f in files]
        files.sort(key=lambda x: os.path.getmtime(os.path.join(fileUploadDir, x)))
        for file in files:
            fulleFilePath = os.path.join(fileUploadDir, file)
            shouldFileInformation.append({"name": file, "tstamp": os.path.getmtime(fulleFilePath) })
        return shouldFileInformation


class FakeRequest():

    def __init__(self, requestType):
        self._type = requestType

    @property
    def method(self):
        return self._type