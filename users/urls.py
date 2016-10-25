from django.conf.urls import url

from . import views

app_name = 'users'
urlpatterns = [
    # /users/
    url(r'^$', views.index, name='index'),
    # /users/3/
    url(r'^(?P<user_id>[0-9]+)/$', views.show, name='show'),
    # /users/new/
    url(r'^new/$', views.new, name='new'),
    # /users/update/
    url(r'^update/$', views.update, name='update'),
    # /users/delete/
    url(r'^delete/$', views.delete, name='delete'),
    # /users/download/
    url(r'^download/$', views.download, name='download'),
]
