from django.shortcuts import render, render_to_response
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
    
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username = request.cleaned_data['username'], \
                                     password = request.cleaned_data['password'])
            if user is not None:
                auth.login(request, user)
                return HttpRespponseRedirect('/account/loggedin')
            else:
                return HttpRespponseRedirect('/account/invalid')
    context['form'] = form
    return render_to_response('login.html', context)

@context_setup
def register(request, context = {}):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_vald():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                return 'password and confirm_password do not match'
            username = form.cleaned_data['username']
            user = auth.models.User.objects.create_user(username = username, password = password)
            user.is_staff = False
            user.save()
            return 'Account Created'
            
@context_setup
def logout(request, context = {}):
    auth.logout(request)
    return 'logged out'