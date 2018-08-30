"""restful URL Configuration

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
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^user/(?P<user_id>\d+)/update$', views.update),
    url(r'^user/(?P<user_id>\d+)/update_password$', views.update_password),
    url(r'^user/(?P<user_id>\d+)/delete_user$', views.delete_user),
    # url(r'^user/(?P<user_id>\d+)$', views.user, name='user')
    ]


# url(r'^$', views.index),
#     url(r'^registration$', views.registration),
#     url(r'^login$', views.login),
#     url(r'^logout$', views.logout),
#     url(r'^user/(?P<user_id>\d+)$', views.user, name='user'),
#     url(r'^user/(?P<user_id>\d+)/opinion$', views.opinion),
#     url(r'^user/(?P<user_id>\d+)/edit$', views.edit),
#     url(r'^user/(?P<user_id>\d+)/update$', views.update),
    # url(r'^user/(?P<user_id>\d+)/delete$', views.delete),
#     url(r'^dashboard$', views.dashboard),