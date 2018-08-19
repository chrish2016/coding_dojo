"""semi_restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),  # takes you to the form page
    url(r'^create/$', views.create),  # processes form page
    url(r'^(?P<user_id>\d+)/$', views.show),  # takes you to user profile page 
    url(r'^(?P<user_id>\d+)/edit/$', views.edit),  # profile page w/ current info
    url(r'^(?P<user_id>\d+)/update/$', views.update),  # processes edited user profile page
    url(r'^(?P<user_id>\d+)/delete/$', views.delete)
    ]