from django import forms

from screener.models import Screener

import json
import logging

logger = logging.getLogger(__name__)

class JobPostForm(forms.Form):
    title = forms.CharField(max_length = 64)
    description = forms.CharField(max_length = 15000, widget = forms.Textarea)
    apply_url = forms.CharField(max_length = 256)
    apply_email_address = forms.EmailField()
    has_screener = forms.BooleanField(required = False)
    #TODO: cut down the number by account most likely
    screeners = forms.ChoiceField(choices=[(s.id, s.name) for s in Screener.objects.all()], required = False)

    """
    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        screeners = Screener.objects.all()
        choices = list()
        for screener in screeners:
            pass

    """
class JobSearchForm(forms.Form):
    key_words = forms.CharField(max_length = 256)
    

class ApplyForm(forms.Form):
    first_name = forms.CharField(max_length = 128)
    last_name = forms.CharField(max_length = 128)
    middle_name = forms.CharField(max_length = 128)
    email_address = forms.EmailField()
    address_street_1 = forms.CharField(max_length = 128)
    address_street_2 = forms.CharField(max_length = 128)
    address_state = forms.CharField(max_length = 64)
    address_city = forms.CharField(max_length = 64)
    address_zip_code = forms.CharField(max_length = 14)
    phone_number = forms.CharField(max_length = 16)
    resume_text = forms.CharField(max_length = 4000, widget = forms.Textarea)
    cover_letter = forms.CharField(max_length = 4000, widget = forms.Textarea)
    #resume_document = forms.CharField(max_length = 128, widget = forms.FileField)

    def __init__(self, post = None, screeners = None, *args, **kwargs):
        super(ApplyForm, self).__init__(*args, **kwargs)
        extra = screeners
        if extra is not None:
            from screener.models import Screener
            if not type(extra) is Screener:
                raise TypeError("screeeners should be of type screener.models.Screener")
            #self.fields['screener_id'] = forms.CharField(widget = forms.HiddenInput, default= extra.id)
            for index, question in enumerate(extra.questions):
                if not hasattr(question, 'answers') and not question.answers is None:
                    self.fields['question_{0}'.format(index)] = forms.CharField(max_length = 128, label = question.question_text)
                else:
                    self.fields['question_{0}'.format(index)] = \
                        forms.ChoiceField(label = question.question_text, \
                                                  choices= [(a.id, a.answer) for a in question.answers],\
                                                  widget = forms.RadioSelect())