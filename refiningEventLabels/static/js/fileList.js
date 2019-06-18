class FileList {
    constructor(fileLoader) {
        this._fileLoader = fileLoader;
        this._files = [];
    }

    _getFilesHtml(download = true) {
        var htmlMarkup = ""
        for (var i = 0; i < this._files.length; i++) {
            var nextFile = this._files[i];
            
            htmlMarkup += `<li id="uploadFile${nextFile.tstamp}" class="list-group-item list-group-item-action">`
            if (download)
                htmlMarkup +=  `<a href="fileDownload?name=${nextFile.name}" >${nextFile.name}</a>`
            else 
                htmlMarkup += `${nextFile.name}`
            htmlMarkup += "</li>"
        }
        return htmlMarkup;
    }

    printFiles(destination) {
        this._fileLoader.getFiles().then(function(data) {
            this._files = data;
            var htmlMarkup = this._getFilesHtml()
            $(destination).empty().append(htmlMarkup)

            $(destination + " li").click(function(e) {
                e.preventDefault()
                $(this).parent().find('li').removeClass('active');
                $(this).addClass('active');
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