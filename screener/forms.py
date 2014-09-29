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
    #json_string = forms.CharField(required = False, widget = forms.HiddenInput)
    #questions = []

    
    def __init__(self, *args, **kwargs):
        clean = kwargs.pop('extra')
        super(ScreenrForm, self).__init__(*args, **kwargs)
        """
        logger.debug('json_string is {0}'.format(clean))
        data = json.load(clean)
        logger.debug('data is {0}'.format(data))
        for key, value in data:
            logger.debug('key is {0}\r\nvalue is {1}'.format(key, value))
            self.fields[key] = forms.CharField()
            if not value is str:
                for k,v in value:
                    self.fields[k] = forms.CharField()"""
    