from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.context_processors import csrf

from agilecar.forms import LoginForm, RegisterForm

import logging
logger = logging.getLogger(__name__)

def context_setup(func):
    def _inner(*args, **kwargs):
        context = dict()
        context['user'] = args[0].user
        context.update(csrf(args[0]))
        context['login_form'] = LoginForm()
        context['register_form'] = RegisterForm()
        kwargs['context'] = context
        return func(*args, **kwargs)
    return _inner