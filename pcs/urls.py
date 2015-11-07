from django.conf.urls import patterns, url
from pcs import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))