from refiningEventLabels.core.apiPage import APIPage
from refiningEventLabels.core.templatePage import TemplatePage
from refiningEventLabels.api.fileUpload import FileUpload
from refiningEventLabels.lib.fileStore import FileStoreConfig

import os

class StartPage(TemplatePage):

    def __init__(self):
        self._methods = ["GET", "POST"]

    def _GET(self, request):
        currentDir = os.path.dirname(__file__)
        destinationTemplate = os.path.join(currentDir, "template", "startPage.html")
        return destinationTemplate

    def _POST(self, request):
        fileUploaderConfig = FileStoreConfig(
            os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))), 'api', 'uploadedFiles'),
            5,
            ['xes', 'csv']
        )
        fileManager = FileUpload(fileUploaderConfig)
        fileManager.execute(request)
        return self._GET(request)
        
    
    def _DELETE(self, request):
        pass