from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^handy_help$', views.index),
    url(r'^log_out$', views.log_out),
    url(r'^add_job$', views.add_job),
    url(r'^add$', views.add),
    url(r'^view_job/(?P<num>\d+)$', views.view_job),
    url(r'^delete/(?P<num>\d+)$', views.delete),
    url(r'^edit_job/(?P<num>\d+)$', views.edit_job),
    url(r'^update/(?P<num>\d+)$', views.update),
    url(r'^add_to_my_job/(?P<num>\d+)$', views.add_to_my_job),
   
   
   
]