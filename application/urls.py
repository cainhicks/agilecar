from django.conf.urls import patterns, url
from application import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^$', views.view, name='view'),
                       )