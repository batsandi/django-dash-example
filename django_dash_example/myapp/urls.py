from django.urls import path
from . import views
from .dash_apps.finished_apps.simple_example import app

urlpatterns = [
    path('', views.home,  name='home'),
]