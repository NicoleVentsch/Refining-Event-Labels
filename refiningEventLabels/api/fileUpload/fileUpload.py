from refiningEventLabels.core.apiPage import APIPage
from refiningEventLabels.lib.eventLogConverter import FileUtility
from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig

import json
import os
import glob

class FileUpload(APIPage):
    
    def __init__(self, config):
        self._methods = ["GET", "POST"]
        self.__fileStore = FileStore(config)
        self._requiredFileName = "eventLog"
        self._allowedFileExtension = set(['csv', 'xes'])
        self._fileConverter = FileUtility('.')

    def _GET(self, request):
        fileInformation = self.__fileStore.filesInfo
        for fileInfo in fileInformation:
            fileInfo["name"] = os.path.basename(fileInfo["name"])
        return json.dumps(fileInformation)

    def _POST(self, request):
        files = request.files
        msg = self._validFileUpload(files)
        if msg != "":
            return msg
        file = files[self._requiredFileName]
        tmpFilePath = os.path.join(os.path.dirname(__file__), "tmp", file.filename)
        file.save(tmpFilePath)
        self.__fileStore.storeFile(tmpFilePath)
        self.__delteFilesOfFolder(os.path.join(os.path.dirname(__file__), "tmp", "*"))
        return self._GET(request)

    def __delteFilesOfFolder(self, path):
        files = glob.glob(path)
        for f in files:
            os.remove(f)
        
    
    def _DELETE(self, request):
        pass

    def _validFileUpload(self, files):
        if self._requiredFileName not in files:
            return "No file Uploaded"
        file = files[self._requiredFileName]
        if file.filename == "":
            "No file selected"        
        elif not self.__allowedFileExtension(file.filename):
            return "File type is not allowed"
        return ""

    def __allowedFileExtension(self, filename):
        return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in self._allowedFileExtension