from django.conf.urls import patterns, url
from screener import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^create/', views.create_screener, name='create'),
                       url(r'^edit/(?P<screener_id>\d+)/$', views.edit, name='edit'),
                       )