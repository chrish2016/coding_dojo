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
    ]