from flask import Flask, render_template, request

import os

from refiningEventLabels.frontend.startPage import StartPage
from refiningEventLabels.api.downloadFile import FileDownload
from refiningEventLabels.api.fileUpload import FileUpload
from refiningEventLabels.lib.fileStore import FileStoreConfig
from refiningEventLabels.api.main import RefiningEventLabels

app = Flask(__name__, template_folder='frontend/template')

@app.route('/refining', methods = ['POST', 'GET'])
def refine():
    
    #a = request.args.get('wn', 0, type=float)
    #b = request.args.get('b', 0, type=int)
     #   print(request.json)
    #return str(a)
    refining = RefiningEventLabels()
    return refining.execute(request)

@app.route('/')
def startup():
    startpage = StartPage()
    return startpage.execute(request)

@app.route('/fileDownload', methods = ['POST', 'GET'])
def fileDownload():
    fileDownloadConfig = FileStoreConfig(
        os.path.join(os.path.dirname(__file__), 'api', 'refinedFiles'),
        5,
        ['xes', 'csv']
    )
    download = FileDownload(fileDownloadConfig)
    return download.execute(request)

@app.route('/fileManager', methods = ['POST', 'GET'])
def fileManger():
    fileUploaderConfig = FileStoreConfig(
        os.path.join(os.path.dirname(__file__), 'api', 'uploadedFiles'),
        5,
        ['xes', 'csv']
    )
    fileManager = FileUpload(fileUploaderConfig)
    return fileManager.execute(request)

@app.route('/refinedFiles', methods = ['GET'])
def fileManagerRefinedFiels():
    fileUploaderConfig = FileStoreConfig(
        os.path.join(os.path.dirname(__file__), 'api', 'refinedFiles'),
        5,
        ['xes', 'csv']
    )
    fileManager = FileUpload(fileUploaderConfig)
    return fileManager.execute(request)