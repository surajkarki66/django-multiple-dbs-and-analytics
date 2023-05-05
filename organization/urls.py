from django.urls import path
from . import views

urlpatterns = [
    path('', views.organization, name='organization'),
]