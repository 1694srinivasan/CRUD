from django.conf.urls import patterns,url
from . import views

urlpatterns = patterns('',
	url(r'^$',views.index),
	url(r'^create$',views.create), 
	url(r'^edit/(?P<id>\d+)$',views.edit),
	url(r'^update/(?P<id>\d+)$',views.update),
	url(r'^delete/(?P<id>\d+)$',views.destroy)
)
