from django.conf.urls import patterns, url
from pcs import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^support/$', views.support, name='support'),
        url(r'^about/$', views.about, name='about'),
        url(r'^statistics/$', views.support, name='statistics'),
        url(r'^getinvolved/$', views.support, name='getinvolved'),
        url(r'^sharedstories/$', views.support, name='sharedstories'),
        url(r'^symptoms/$', views.support, name='symptoms'),
        url(r'^login/$', views.support, name='login'),)