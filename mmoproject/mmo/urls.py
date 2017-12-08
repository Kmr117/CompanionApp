from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user/$', views.userView.as_view(), name='user'),
    url(r'^user/(?P<name>\w+)/$', views.userView.as_view(), name='userFind'),
    url(r'^usearch_result/(?P<target>\w+)/$', views.usearch_result, name='usearch_result'),
    url(r'^character/$', views.characterView.as_view(), name = 'character'),
    url(r'^character/(?P<charName>\w+)/$', views.characterView.as_view(), name='characterFind'),
    url(r'^user/addUser/$', views.addUser,name = 'addUser'),
    url(r'^character/items/$', views.character2, name='items'),

]