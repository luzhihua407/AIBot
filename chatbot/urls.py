from django.urls import path

from qabot import HotLoad
from . import views

urlpatterns = [
    path('api', views.api, name='api'),
]