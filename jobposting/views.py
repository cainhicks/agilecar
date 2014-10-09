from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone

from jobposting import forms
from jobposting.models import Job
from screener.forms import ScreenrForm
from screener.models import Screener, ScreenerQuestion, ScreenerAnswer, load_screener
from agilecar import objectmapper
from agilecar.decorators import context_setup

import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('index')

@context_setup
def post_job(request, context = {}):
    form = None
    screeners = Screener.objects.all()
    if request.method == 'POST':
        form = forms.JobPostForm(request.POST)
        if form.is_valid():
            job = Job()
            objectmapper.map(form, job)
            job.is_active = True
            job.is_approved = True #for now...
            job.created_date = timezone.now()
            job.posted_date = timezone.now()
            job.expire_date = timezone.now()
            
            if form.cleaned_data['has_screener'] == True:
                screener = Screener.objects.get(id = form.cleaned_data['screeners'])
                job.screener = screener
            job.save()
            
            return HttpResponse(str(form.cleaned_data))
    else:
        form = forms.JobPostForm()
    context['form'] = form
    context['screeners'] = screeners
    return render(request, 'jobposting/postjob.html', context)

@context_setup
def view_job(request, job_id, context = {}):
    job = Job.objects.get(id = job_id)
    context['job'] = job
    return render(request, 'jobposting/view.html', context)

@context_setup
def apply(request, job_id, context = {}):
    
    #TODO: Add error handling
    job = Job.objects.get(id = job_id)
    if job.has_screener:
        job.screener = load_screener(job.screener.id)
    form = forms.ApplyForm(None, screeners = job.screener)
    if request.method == 'POST':
        form = forms.ApplyForm(request.POST, screeners = job.screener)
        if form.is_valid():
            app = Application()
            objectmapper.map(form, app)
            app.job = job
            app.created_date = timezone.now()
            app.save()
            return HttpResponse(str(app))
    context['form'] = form
    context['job'] = job
    return render(request, 'jobposting/apply.html', context)

@context_setup
def search(request, context = {}):
    form = None
    if request.method == 'POST':
        form = forms.JobSearchForm(request.POST)
        if form.is_valid():
            jobs = dict()
            filtered_jobs = None
            for key_word in form.cleaned_data['key_words'].split(','):
                filtered_jobs = Job.objects.filter(description__contains = key_word)
                if filtered_jobs is not None:
                    for job in filtered_jobs:
                        if not job.id in jobs:
                            jobs[job.id] = job
            context['form'] = form
            context['jobs'] = jobs.values()
            return render(request, 'jobposting/search.html', context)
    else:
        form = forms.JobSearchForm()
    context['form'] = form
    return render(request, 'jobposting/search.html', context)