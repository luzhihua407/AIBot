from django.urls import path

from qabot import HotLoad
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tall', views.tall, name='tall'),
    path('append', HotLoad.load, name='load'),
]