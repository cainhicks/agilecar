from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'agilecar.views.index', name='index'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jobposting/', include('jobposting.urls')),
    url(r'^application/', include('application.urls')),
    url(r'^screeners/', include('screener.urls')),

    #auth urls
    url(r'^account/login/$', 'agilecar.views.login'),
    url(r'^account/register/$', 'agilecar.views.register'),
    #url(r'^account/logout/$', 'agilecar.views.logout'),
    #url(r'^account/loggedin/$', 'agilecar.views.loggedin'),
    #url(r'^account/invalid/$', 'agilecar.views.invalid_login'),
)

