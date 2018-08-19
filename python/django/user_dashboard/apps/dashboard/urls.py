from django.conf.urls import url
from . import views           # This line is new!
    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^session$', views.session),
    url(r'^logout/$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^admin$', views.admin),
    url(r'^user/(?P<user_id>\d+)/$', views.show),
    url(r'^user/(?P<user_id>\d+)/edit/$', views.edit),  # profile page w/ current info
    url(r'^user/(?P<user_id>\d+)/update$', views.update),  # processes edited user profile page
    url(r'^user/(?P<user_id>\d+)/delete/$', views.delete),
    url(r'^user/(?P<user_id>\d+)/comment/$', views.comment),
    url(r'^user/(?P<user_id>\d+)/post/$', views.post),
    url(r'^user/(?P<user_id>\d+)/delete_comment/$', views.delete_comment),
    url(r'^new_user$', views.new_user),
    url(r'^process_user$', views.process_user)
]