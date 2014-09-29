

def get_questions(request):
    data = request.POST
    questions = dict()
    for key, value in data.iteritems():
        if 'questionText' in key or \
            'multipleChoiceAnswerText_' in key:
            questions[key] = value
    return questions

def find_question_id(questions, question_index):
    question_text = 'questionText_{0}'.format(question_index)
    if question_text in questions:
        return question_text