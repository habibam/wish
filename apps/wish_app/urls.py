from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^addProduct/(?P<id>\d+)$', views.addProduct),
    url(r'^userPage$', views.userPage),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^api$', views.api),
]
