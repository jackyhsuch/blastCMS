from django.conf.urls import url

from . import views

app_name = 'attendance'
urlpatterns = [
    # /users/
    url(r'^$', views.index, name='index'),
    # /users/new/
    url(r'^new/$', views.new, name='new'),
]
