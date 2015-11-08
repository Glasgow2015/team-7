from django.conf.urls import patterns, url
from pcs import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^support/$', views.support, name='support'),
        url(r'^about/$', views.about, name='about'),
        url(r'^statistics/$', views.statistics, name='statistics'),
        url(r'^getinvolved/volunteer_registration/$', views.volunteer_registration, name = 'volunteer_registration'),
        url(r'^getinvolved/$', views.getinvolved, name='getinvolved'),
        url(r'^sharedstories/$', views.sharedstories, name='sharedstories'),
        url(r'^symptoms/$', views.symptoms, name='symptoms'),
        url(r'^login/$', views.login, name='login'),
        url(r'^donate/$', views.donate, name='donate'),
        url(r'^map/$', views.map, name='map'),)
