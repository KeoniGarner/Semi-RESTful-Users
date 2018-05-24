from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name="users"),
    re_path(r'^users/$', views.index, name="users"),
    re_path(r'^users/new/$', views.new, name="new"),
    re_path(r'^users/(?P<id>\d+)/edit/$', views.edit, name="edit"),
    re_path(r'^users/(?P<id>\d+)/show/$', views.show, name="show"),
    re_path(r'^users/create/$', views.create, name="create"),
    re_path(r'^users/(?P<id>\d+)/destroy/$', views.destroy, name="destroy"),
    re_path(r'^users/update/$', views.update, name="update"),
]