from refiningEventLabels.core.apiPage import APIPage
from refiningEventLabels.lib.eventLogConverter import FileUtility
from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig

from flask import jsonify
import os

class FileUpload(APIPage):
    
    def __init__(self, config):
        self._methods = ["GET", "POST"]
        self.__fileStore = FileStore(config)

    def _GET(self):
        fileInformation = self.__fileStore.FilesInfo
        return jsonify(fileInformation)

    def _POST(self):
        pass
    
    def _DELETE(self):
        pass