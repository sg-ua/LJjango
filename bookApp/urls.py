from django.contrib import  admin
from django.urls import  path, re_path
from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    #re_path('^([0-9]+)/$', views.detail, name='detail')
    path('<int:id>/', views.detail, name='detail')
]