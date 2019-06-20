from refiningEventLabels.core.apiPage import APIPage
from refiningEventLabels.lib.eventLogConverter import FileUtility
from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig

import json
import os
import glob

class RefiningEventLabels(APIPage):

    def __init__(self):
        self._methods = ["POST", "GET"]

    def _GET(self, request):
        return "GET"

    def _POST(self, request):
        print(request.json)
        return json.dumps(request.json)

    def _DELETE(self, request):
        pass

    def _DEFAULT(self, request):   
        pass 


