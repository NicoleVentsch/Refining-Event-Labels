from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig
from refiningEventLabels.core import FilePage

import os 

class FileDownload(FilePage):

    def __init__(self, config):
        self._methods = ["GET", "POST"]
        self.__fileStore = FileStore(config)

    def _GET(self, request):
        name = request.args.get('name')
        fileInformation = self.__fileStore.filesInfo
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), "refinedFiles", name)
        #return "No file found"
    
    def _POST(self, request):
        pass
        
    
    def _DELETE(self, request):
        pass
        