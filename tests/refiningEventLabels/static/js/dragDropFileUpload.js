window.onload = function() {
    var fileUploadController = new FileUploader('drop-zone', 'js-upload-form')
    fileUploadController.init()
}

class FileUploader {

    constructor(dropZone, uploadForm) {
        this._dropZone = document.getElementById(dropZone);
        this._uploadForm = document.getElementById(uploadForm)
    }

    init() {
        this.initializeUploadForm()
        this.initializeUploadDropZone()
    }

    initializeUploadForm() {
        this._uploadForm.addEventListener('submit', function(e) {
            var uploadFiles = document.getElementById('js-upload-files').files;
            e.preventDefault()
            this._startUpload(uploadFiles)
        }.bind(this))
    }

    initializeUploadDropZone() {
        this._dropZone.ondrop = function(e) {
            e.preventDefault();
            this.className = 'upload-drop-zone';
           this._startUpload(e.dataTransfer.files);
        }.bind(this)
    
        this._dropZone.ondragover = function() {
            this.className = 'upload-drop-zone drop';
            return false;
        }
    
        this._dropZone.ondragleave = function() {
            this.className = 'upload-drop-zone';
            return false;
        }
    }

    _startUpload(files) {

        // Ein Objekt um Dateien einzulesen
        var reader = new FileReader();
        
        var senddata = new Object();
        // Auslesen der Datei-Metadaten
        senddata.name = files[0].name;
        senddata.date = files[0].lastModified;
        senddata.size = files[0].size;
        senddata.type = files[0].type;

        // Wenn der Dateiinhalt ausgelesen wurde...
        reader.onload = function(theFileData) {
            senddata.fileData = theFileData.target.result; // Ergebnis vom FileReader auslesen
      

            $.post("fileManager", senddata ).done(function(data){
                alert(data)
            });
          }
      
          // Die Datei einlesen und in eine Data-URL konvertieren
        reader.readAsDataURL(files[0]);

    }
}


/*+ function($) {
    'use strict';

    var dropZone = document.getElementById('drop-zone');
    var uploadForm = document.getElementById('js-upload-form');

    var startUpload = function(files) {
        console.log(files)
        $('#file-name-upload').val(files[0].name)
    }

    uploadForm.addEventListener('submit', function(e) {
        var uploadFiles = document.getElementById('js-upload-files').files;
        e.preventDefault()

        startUpload(uploadFiles)
    })

    dropZone.ondrop = function(e) {
        e.preventDefault();
        this.className = 'upload-drop-zone';

        startUpload(e.dataTransfer.files)
    }

    dropZone.ondragover = function() {
        this.className = 'upload-drop-zone drop';
        return false;
    }

    dropZone.ondragleave = function() {
        this.className = 'upload-drop-zone';
        return false;
    }

}(jQuery);*/