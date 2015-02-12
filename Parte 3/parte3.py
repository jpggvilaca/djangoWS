# app/views.py

###1
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
	

###2 app/urls.py


from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)

###3  mysite/urls.py

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

###4
###5