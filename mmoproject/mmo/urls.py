from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user/$', views.user, name='user'),
    url(r'^user/(?P<name>\w+)/$', views.user, name='user'),
    url(r'^usearch_result/(?P<target>\w+)/$', views.usearch_result, name='usearch_result'),
    url(r'^character/(?P<charName>\w+)/$', views.character, name='character')
]