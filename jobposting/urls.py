from django.conf.urls import patterns, url
from jobposting import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^postajob/', views.post_job, name='postajob'),
                       url(r'^job/(?P<job_id>\d+)/$', views.view_job, name='job'),
                       url(r'^apply/(?P<job_id>\d+)/$', views.apply, name='apply'),
                       url(r'^search/', views.search, name='search'),
                       )