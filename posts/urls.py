from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^(?P<id>\d+)/$', views.details, name='details'),
    url(r'^(?P<id>\d+)/upvote$', views.upvote, name='upvote'),
    url(r'^(?P<id>\d+)/downvote$', views.downvote, name='downvote')
)