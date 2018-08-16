from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'^topics/$', views.topics, name='topics'),
    ]