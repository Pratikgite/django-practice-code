from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    
    url(r'^(?P<id>[0-9]+)/$', views.emp_detail),
]