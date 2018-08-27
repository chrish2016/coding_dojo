from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^user/(?P<user_id>\d+)$', views.user, name='user'),
    url(r'^user/(?P<user_id>\d+)/opinion$', views.opinion),
    url(r'^user/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^user/(?P<user_id>\d+)/update$', views.update),
    url(r'^user/(?P<user_id>\d+)/delete$', views.delete),
    url(r'^dashboard$', views.dashboard),
    # url(r'^book/add$', views.add),
    # url(r'^book/(?P<book_id>\d+)/$', views.bookpage),
    # url(r'^book/(?P<book_id>\d+)/minireview$', views.minireview),
    # url(r'^book/(?P<book_id>\d+)/delete', views.delete)
]