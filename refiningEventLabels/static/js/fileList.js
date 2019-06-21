class FileList {
    constructor(fileLoader, downloadable = true) {
        this._fileLoader = fileLoader;
        this._files = [];
        this._file = "";
        this._downloadable = downloadable;
    }

    _getFilesHtml() {
        var htmlMarkup = ""
        for (var i = 0; i < this._files.length; i++) {
            var nextFile = this._files[i];
            htmlMarkup += `<li id="uploadFile${nextFile.tstamp}" class="list-group-item list-group-item-action">${nextFile.name}</li>`
        }
        return htmlMarkup;
    }

    printFiles(destination) {
        this._fileLoader.getFiles().then(function(data) {
            this._files = data;
            this.file = this._files[0];
            var htmlMarkup = this._getFilesHtml()
            $(destination).empty().append(htmlMarkup)
            var me = this;
            $(destination + " li").click(function(e) {
                e.preventDefault()
                $(this).parent().find('li').removeClass('active');
                $(this).addClass('active');
                me.file = $(this).val();
                if (me._downloadable) {
                    var urlAppendix = `fileDownload?name=${$(this).text()}`;
                    window.location.href += urlAppendix;
                    //$(this).parent().find('li').
                }
            });
        }.bind(this));

    }
}

class FileLoader {
    constructor(fileUrl) {
        this._fileUrl = fileUrl;
    }

    getFiles() {
        var me = this;
        return new Promise( function(resolve, reject) {   
            $.getJSON(me._fileUrl, function(data) {
                resolve(data);
            }.bind(this));
        });
    }
}