from django.conf.urls import url

from api import views

urlpatterns = [
    url(r'^1/comment/(?P<app>\w+)/(?P<key>\d+)/(?P<sessionid>.*)/' +
        '(?P<offset>\d+)/$',
        views.get_comment),
    url(r'^1/rating/(?P<app>\w+)/(?P<key>\d+)/(?P<sessionid>.*)/$',
        views.get_rating),

    url(r'^1/vote/$', views.vote_rating),
]
