class ValuePicker {
    constructor(id, name) {
        this._id = id;
        this._name = name;
        this._value = 0.5;
    }

    _createHtml() {
        return `<div id="container${this._id}">
                    <label for="${this._id}">${this._name}: </label><input style="width: 25%" type="text" value="0.5"></input>
                    <input type="range" class="custom-range" min="0" max="1" step="0.1" id="${this._id}">  
                </div>`;
    }

    get value() {
        return this._value;
    }

    create(destination) {
        $(destination).append(this._createHtml());
        var me = this;
        $(`#container${me._id} input`).change(function(changedValue) {
            $(`#container${me._id} input`).each(function() {
                me._value = changedValue.target.value;
                if (me._value > 1)
                    me._value = 1;
                else if (me._value < 0)
                    me._value = 0;
                me._value = Math.round(me._value * 10) / 10;
                $(this).val(me._value);
            });
        })
    }
} 