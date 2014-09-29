from django import forms
import json
import logging

logger = logging.getLogger(__name__)

class JobPostForm(forms.Form):
    title = forms.CharField(max_length = 64)
    description = forms.CharField(max_length = 15000, widget = forms.Textarea)
    apply_url = forms.CharField(max_length = 256)
    apply_email_address = forms.EmailField()
    has_screener = forms.BooleanField()
    #screeners = forms.MultipleChoiceField(widget = forms.Select)
    
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