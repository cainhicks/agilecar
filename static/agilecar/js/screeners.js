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
    var container = createContinerElement(id, 'questionVisible');
    id = 'questionText_' + questionIndex.toString();
    var label = createLabel(id, 'Question Text');
    var input = createInput(id, 'text', '');
    container.appendChild(label);
    container.appendChild(input);
    document.getElementById('screenerQuestionPlaceHolder').appendChild(container).appendChild(createBr());
}

function buildMulipleChoiceQuestion() {
    var id = createId();
    var container = createContinerElement(id, 'questionVisible');
    id = 'questionText_' + questionIndex.toString();
    var label = createLabel(id, 'Question Text');
    var questionInput = createInput(id, 'text', '');
    var answerInput = createInput(createAnswerId(), 'text', '');
    var button = createInput('btnAdd', 'button', 'Add Answer');
    button.setAttribute('onclick', 'addQuestionAnswer()');
    container.appendChild(label);
    container.appendChild(questionInput);
    container.appendChild(answerInput);
    container.appendChild(button);
    document.getElementById('screenerQuestionPlaceHolder')
    .appendChild(container)
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
    container.appendChild(label);
    container.appendChild(input);
    container.appendChild(createBr());
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