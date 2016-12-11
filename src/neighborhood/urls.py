
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from neighborhood import views

urlpatterns = [
    url(r'^neighborhood/$', views.neighborhood_list, name='neighborhood-list'),
    url(r'^neighborhood/(?P<id>\d+)/$', views.neighborhood_details, name='neighborhood-details'),
    url(r'^neighborhood/(?P<id>\d+)/delete/$', views.neighborhood_delete, name='neighborhood-delete'),
]
