from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^words/process$', views.process),
    # url(r'^result$', views.result),
    url(r'^words/reset$', views.reset)
]