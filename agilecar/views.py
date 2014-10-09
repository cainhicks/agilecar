from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone
from django.contrib import auth


from agilecar import forms
from agilecar.decorators import context_setup

import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request, 'jobposting/index.html', None)

@context_setup
def login(request, context = {}):
    logger.debug('hit login')
    form = forms.LoginForm()
    logger.debug(request.method)
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        logger.debug(form.is_valid())
        if form.is_valid():
            logger.debug(form.cleaned_data['login_username'])
            logger.debug(form.cleaned_data['login_password'])
            user = auth.authenticate(username = form.cleaned_data['login_username'], \
                                     password = form.cleaned_data['login_password'])
            if user is not None:
                logger.debug('user is not none')
                auth.login(request, user)
                return redirect('/jobposting/search/')
            else:
                logger.debug('user is none')
    context['form'] = form
    return render_to_response('login.html', context)

@context_setup
def register(request, context = {}):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_vald():
            password = form.cleaned_data['register_password']
            confirm_password = form.cleaned_data['confirm_password']
            if password == confirm_password:
                username = form.cleaned_data['register_username']
                user = auth.models.User.objects.create_user(username = username, password = password)
                user.is_staff = False
                user.save()
                return HttpResponse('account created')
    context['form'] = form
    return render(request, 'account/register.html', context)
            
@context_setup
def logout(request, context = {}):
    auth.logout(request)
    return redirect('/jobposting/search')