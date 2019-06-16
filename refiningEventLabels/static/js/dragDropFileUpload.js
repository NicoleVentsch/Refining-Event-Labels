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

        var data = new FormData();
        $.each($('files'), function(i, file) {
            data.append('file-'+i, file);
        });

        console.log(files)
        //$('#file-name-upload').val(files[0].name)
        $.post("fileManager", { eventLog: data } ).done(function(data){
            alert(data)
        });
        return false;
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