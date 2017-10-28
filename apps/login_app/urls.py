from django.conf.urls import url
from . import views
from django.http import HttpResponse
def test(request):
    return HttpResponse('app')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^userPage$', views.userPage),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]
