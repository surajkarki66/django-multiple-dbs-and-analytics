from django.urls import path
from . import views

urlpatterns = [
    path('', views.university, name='university'),
]