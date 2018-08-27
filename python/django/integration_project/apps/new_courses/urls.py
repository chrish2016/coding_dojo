from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    # url(r'^register$', views.register),
    # url(r'^login$', views.login),
    # url(r'^logout$', views.logout),
    # url(r'^show$', views.show),
    # url(r'^user/(?P<user_id>\d+)$', views.show),
    # url(r'^book/form$', views.bookform),
    url(r'^add$', views.add),
    url(r'^(?P<course_id>\d+)/remove$', views.remove),
    url(r'^(?P<course_id>\d+)/delete$', views.delete),
    # url(r'^book/(?P<book_id>\d+)/$', views.bookpage),
    # url(r'^book/(?P<book_id>\d+)/minireview$', views.minireview),
    # url(r'^book/(?P<book_id>\d+)/delete', views.delete)
]
