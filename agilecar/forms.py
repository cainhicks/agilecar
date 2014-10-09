from django import forms
import logging

logger = logging.getLogger(__name__)


class LoginForm(forms.Form):
    login_username = forms.CharField(max_length = 128)
    login_password = forms.CharField(widget = forms.PasswordInput())

class RegisterForm(forms.Form):
    register_username = forms.CharField(label = 'Username')
    register_password = forms.CharField(label = 'Password', widget = forms.PasswordInput())
    confirm_password = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput())