from django.conf.urls import url
from django.urls import path

from app import views

app_name = 'app'

urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
]
