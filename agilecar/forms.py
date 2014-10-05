from django import forms
import logging

logger = logging.getLogger(__name__)


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 128)
    password = forms.CharField(widget = forms.PasswordInput())

class RegisterForm(forms.Form):
    username = forms.CharField(label = 'Username')
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    confirm_password = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput())