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
    # /users/attendance/
    url(r'^attendance/$', views.attendance, name='attendance'),
    # /users/upload/
    url(r'^upload/$', views.upload, name='upload'),
    # /users/addattendancemember/
    url(r'add_attendance_member/$', views.add_attendance_member, name='add_attendance_member'),
]
