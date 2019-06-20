$(document).ready(function(){
    var fileLoader = new FileLoader(window.location.href + "fileManager");
    var filePrinter = new FileList(fileLoader);
    filePrinter.printFiles("#uploadedFiles");

    var fileLoader = new FileLoader(window.location.href + "refinedFiles");
    var filePrinter = new FileList(fileLoader);
    filePrinter.printFiles("#refinedFiles");

    var vertPicker = new ValuePicker("horizontalThreshold", "Horizontal threshold");
    var horPicker = new ValuePicker("verticalThreshold", "Vertical threshold");
    var vmPicker = new ValuePicker("costMatchedLabels", "matched labels weight");
    var wsPicker = new ValuePicker("structuralCost", "structural cost weight");
    var wnPicker = new ValuePicker("costNonMatched", "non-matched labels weight");

    vertPicker.create('#customize');
    horPicker.create('#customize');
    vmPicker.create('#customize');
    wsPicker.create('#customize');
    wnPicker.create('#customize');
})