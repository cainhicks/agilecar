from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.utils import timezone

from jobposting import forms

import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse('index')


def post_job(request):
    form = None
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
            job.save()
            return HttpResponse(str(form.cleaned_data))
    else:
        form = forms.JobPostForm()
    return render(request, 'jobposting/postjob.html', {'form': form})

def view_job(request, job_id):
    job = Job.objects.get(id = job_id)
    return render(request, 'jobposting/view.html', {'job': job})

def apply(request, job_id):
    form = forms.ApplyForm()
    #TODO: Add error handling
    job = Job.objects.get(id = job_id)
    if request.method == 'POST':
        form = forms.ApplyForm(request.POST)
        if form.is_valid():
            app = Application()
            objectmapper.map(form, app)
            app.job = job
            app.created_date = timezone.now()
            app.save()
            return HttpResponse(str(app))
    return render(request, 'jobposting/apply.html', {'form': form, 'job': job})


def search(request):
    form = None
    if request.method == 'POST':
        form = forms.JobSearchForm(request.POST)
        if form.is_valid():
            jobs = Job.objects.filter(description__contains = form.cleaned_data['key_words'])
            return render(request, 'jobposting/search.html', {'form': form, 'jobs': jobs})
    else:
        form = forms.JobSearchForm()
    return render(request, 'jobposting/search.html', {'form': form})