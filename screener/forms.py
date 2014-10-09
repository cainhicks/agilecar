from django import forms
import json
import logging

logger = logging.getLogger(__name__)

class ScreenrForm(forms.Form):
    QUESTION_TYPES = (
                      ('ff', 'Free Form'),
                      ('mc', 'Multiple Choice')
                      )
    name = forms.CharField()

    
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(ScreenrForm, self).__init__(*args, **kwargs)
        logger.debug(str(extra))

        for key in extra:
            logger.debug('key ' + key)
            self.fields[key] = forms.CharField()

    def questions_as_dict(self):
        extra = dict()
        not_found = dict()
        for key, value in self.cleaned_data.items():
            if key.startswith('questionText'):
                extra[key] = dict()
                extra[key][key] = value
            elif key.startswith('multipleChoiceAnswerText_'):
                question_key = self.get_question_key(key)
                if question_key in extra:
                    extra[question_key][key] = value
                else:
                    if question_key not in not_found:
                        not_found[question_key] = dict()
                    not_found[question_key][key] = value
        if len(not_found) > 0:
            for key, value in not_found.items():
                for k, v in value.items():
                    extra[key][k] = value
        return extra

    def get_question_key(self, lookup):
        return 'questionText_{0}'.format(lookup.split('_')[1])
    

class ScreenerApplyForm(forms.Form):
    name = forms.CharField()

class ScreenerAnswerForm(forms.Form):
    screener_answer = forms.CharField(max_length = 512)

