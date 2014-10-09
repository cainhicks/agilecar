var questionIndex = 0;
var answerIndex = 0;

function buildScreenerQuestions() {
    if ($('#screenerMultipleChoice').is(':checked')) {
        buildMulipleChoiceQuestion();
    }
    else {
        buildFreeFormQuestion();
    }
}

function buildFreeFormQuestion() {
    var id = createId()
    var row = createContinerElement('row' + id, 'row');
    var container = createContinerElement(id, 'col-md-4');
    id = 'questionText_' + questionIndex.toString();
    var label = createLabel(id, 'Question Text');
    var input = createInput(id, 'text', '');
    container.appendChild(label);
    container.appendChild(input);
    row.appendChild(container);
    document.getElementById('screenerQuestionPlaceHolder').appendChild(row).appendChild(createBr());
}

function buildMulipleChoiceQuestion() {
    var id = createId();
    var row = createContinerElement('row' + id, 'row');
    var container = createContinerElement(id, 'col-md-4');
    id = 'questionText_' + questionIndex.toString();
    var label = createLabel(id, 'Question Text');
    var questionInput = createInput(id, 'text', '');
    var answer_id = createAnswerId();
    var answer_label = createLabel(answer_id, "Answer Text");
    var answerInput = createInput(answer_id, 'text', '');
    var button = createInput('btnAdd', 'button', 'Add Answer');
    button.setAttribute('onclick', 'addQuestionAnswer()');
    container.appendChild(label);
    container.appendChild(questionInput);
    container.appendChild(createBr());
    container.appendChild(createBr());
    container.appendChild(answer_label);
    container.appendChild(answerInput);
    container.appendChild(createBr());
    container.appendChild(createBr());
    container.appendChild(button);
    row.appendChild(container);
    document.getElementById('screenerQuestionPlaceHolder')
    .appendChild(row)
    .appendChild(createBr());
    
}

function createContinerElement(id, cls) {
    var container = document.createElement("div");
    container.setAttribute('id', id);
    container.setAttribute('class', cls);
    return container;
}

function createLabel(id, txt) {
    var label = document.createElement('label');
    label.setAttribute('for', id);
    label.textContent= txt;
    return label;
}

function createInput(id, type, value) {
    var input = document.createElement('input');
    input.setAttribute('id', id);
    input.setAttribute('name', id);
    input.setAttribute('type', type);
    input.setAttribute('value', value);
    return input;
}

function createBr() {
    var br = document.createElement('br');
    return br;
}

function addQuestionAnswer() {
    var container = document.getElementById(getId());
    var id = createAnswerId();
    var label = createLabel(id, 'Answer Text');
    var input = createInput(id, 'text', '');
    var btn = document.getElementById('btnAdd');
    container.insertBefore(label, btn);
    container.insertBefore(input, btn);
    container.insertBefore(createBr(), btn);
    container.insertBefore(createBr(), btn);
}

function createId() {
    questionIndex++;
    return getId();
}

function getId() {
    return 'screenerQuestion_' + questionIndex.toString();
}

function createAnswerId() {
    answerIndex++;
    return 'multipleChoiceAnswerText_' + questionIndex.toString() + '_' + answerIndex.toString();
}

function createJson() {
    var arrJson = {};
    if (questionIndex > 0) {
        for (var i = 1; i <= questionIndex; i++) {
            var qId = 'questionText_' + i.toString();
            var question = document.getElementById(qId);
            arrJson[qId] = {};
            arrJson[qId][qId] = question.value;
            var aId = 'multipleChoiceAnswerText_' + i.toString() + '_1';
            var answer = document.getElementById(aId);
            if (answer != null && answer != 'undefined') {
                for (var c = 1; c <= 10; c++) {
                    aId = 'multipleChoiceAnswerText_' + i.toString() + '_' + c.toString();
                    answer = document.getElementById(aId);
                    //alert(aId);
                    if (answer != null && answer != 'undefined') {
                        arrJson[qId][aId] = answer.value;
                    }
                }
            }
        }
        var strJson = encodeURIComponent(JSON.stringify(arrJson));
        document.getElementById('json_string').value = strJson;
    }
}