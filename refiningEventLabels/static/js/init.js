$(document).ready(function(){
    var fileLoader = new FileLoader(window.location.href + "fileManager");
    var filePrinter = new FileList(fileLoader);
    filePrinter.printFiles("#uploadedFiles");

    var fileLoader = new FileLoader(window.location.href + "refinedFiles");
    var filePrinter = new FileList(fileLoader);
    filePrinter.printFiles("#refinedFiles");
})