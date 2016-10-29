from django.conf.urls import url

from . import views

app_name = 'attendance'
urlpatterns = [
    # /attendance/
    url(r'^$', views.index, name='index'),
    # /attendance/new/
    url(r'^new/$', views.new, name='new'),
    # /attendance/3/
    url(r'^(?P<event_id>[0-9]+)/$', views.show, name='show'),
]
