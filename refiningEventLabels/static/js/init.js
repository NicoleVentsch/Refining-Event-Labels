$(document).ready(function(){
    var fileLoader = new FileLoader(window.location.href + "fileManager");
    var uploadedFiles = new FileList(fileLoader, false);
    uploadedFiles.printFiles("#uploadedFiles");

    var fileLoader = new FileLoader(window.location.href + "refinedFiles");
    var refinedFiles = new FileList(fileLoader, true);
    refinedFiles.printFiles("#refinedFiles");

	var horPicker = new ValuePicker("horizontalThreshold", "Horizontal threshold");
	var vertPicker = new ValuePicker("verticalThreshold", "Vertical threshold");
    var vmPicker = new ValuePicker("costMatchedLabels", "matched labels weight");
    var wsPicker = new ValuePicker("structuralCost", "structural cost weight");
    var wnPicker = new ValuePicker("costNonMatched", "non-matched labels weight");

    vertPicker.create('#customize');
    horPicker.create('#customize');
    vmPicker.create('#customize');
    wsPicker.create('#customize');
    wnPicker.create('#customize');

    $('#submit').click(function(e) {
        var data = {
            fileName: uploadedFiles._file,
            hor : horPicker.value,
			vert: vertPicker.value,
            wm: vmPicker.value,
            ws: wsPicker.value,
            wn: wnPicker.value,
            candidateLabel: $('#candidateLabels').val()

        };
        $.post('/refining', data, function(data) {
            location.reload(); 
        });
    })
})
