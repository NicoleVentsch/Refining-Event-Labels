from refiningEventLabels.core.apiPage import APIPage
from refiningEventLabels.lib.eventLogConverter import FileUtility
from refiningEventLabels.lib.fileStore import FileStore, FileStoreConfig
from refiningEventLabels.lib.objects import customParameters

from refiningEventLabels.lib.main import main

import json
import os
import glob

class RefiningEventLabels(APIPage):

    def __init__(self):
        self._methods = ["POST", "GET"]

    def _GET(self, request):
        return "GET"

    def _POST(self, request):
        params = customParameters(["decide", "examine casually"], float(request.form['vert']), float(request.form['hor']), float(request.form['ws']), float(request.form['vm']), float(request.form['wn']))
        refinedFile = request.form['fileName']
        fileAccess = FileStore(FileStoreConfig(os.path.join(os.path.dirname(os.path.dirname(__file__)),  'uploadedFiles'), 5,['xes', 'csv']))
        

        for files in fileAccess.filesInfo:
            if os.path.basename(files["name"]) == refinedFile:
                eventLogFile = files["name"]
        
        fileUtility = FileUtility(os.path.join(os.path.dirname(os.path.dirname(__file__)),  'refinedFiles'))
        print(os.path.join(os.path.dirname(os.path.dirname(__file__)),  'refinedFiles'))
        eventLog = fileUtility.getEventLogFromFile(eventLogFile)

        resultEventLog = main(params, eventLog)
        fileUtility.createFile(resultEventLog, 'refined.xes', '.xes')
        return "refined"


        
    #b = request.args.get('b', 0, type=int)
     #   print(request.json)
        return str(refinedFile)

    def _DELETE(self, request):
        pass

    def _DEFAULT(self, request):   
        pass 


