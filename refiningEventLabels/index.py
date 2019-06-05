from flask import Flask, render_template, request

import os

from refiningEventLabels.frontend.startPage import StartPage
from refiningEventLabels.api.fileUpload import FileUpload
from refiningEventLabels.lib.fileStore import FileStoreConfig

app = Flask(__name__, template_folder='frontend/template')
@app.route('/')
def startup():
    startpage = StartPage()
    return startpage.execute(request)

<<<<<<< HEAD
@app.route('/fileManager')
def fileManger():
    fileUploaderConfig = FileStoreConfig(
        os.path.join(os.path.dirname(__file__), 'api', 'uploadedFiles '),
=======
@app.route('/fileManager', methods = ['POST', 'GET'])
def fileManger():
    fileUploaderConfig = FileStoreConfig(
        os.path.join(os.path.dirname(__file__), 'api', 'uploadedFiles'),
>>>>>>> f3667f908a6380302f380704bda23c5a17221b8f
        5,
        ['xes', 'csv']
    )
    fileManager = FileUpload(fileUploaderConfig)
    return fileManager.execute(request)