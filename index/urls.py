from django.conf.urls import url
from .views import *
from django.contrib.auth.views import login
urlpatterns = [

    url(r'^$', index_views, name='index'),
    url(r'^login/$', index_login, name='login'),
    url(r'^logout/$', index_logout, name='logout'),
    url(r'^register/$',index_register,name='register'),
    url(r'^test/$', test),
    url(r'^modelbase/$',index_modelbase),
]