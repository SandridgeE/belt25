from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^success$', views.success),
    url(r'^add_new$', views.add_new),
    url(r'^new$', views.new),
    url(r'^join$', views.join),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^update/(?P<id>\d+)$', views.update),
]