from django import views
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth.views import login
from .learning_logs import views

#urlpatterns = [url(r'^admin/', include(admin.site.urls)),]
# urlpatterns = [url(r'^admin/', include(admin.site.urls)),
#        url(r'', include('learning_logs.urls', namespace='learning_logs')),]
       urlpatterns = [url(r'^admin/', include(admin.site.urls)),
       url(r'^users/', include('users.urls', namespace='users')),
       url(r'', include('learning_logs.urls', namespace='learning_logs')),
               url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
       url(r'^new_topic/$', views.new_topic, name='new_topic'),
       url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
       url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
    name='edit_entry'),
       url(r'^login/$', login, {'template_name': 'users/login.html'}, name='login'),
       url(r'^logout/$', views.logout_view, name='logout'),
       url(r'^register/$', views.register, name='register'),
   ]