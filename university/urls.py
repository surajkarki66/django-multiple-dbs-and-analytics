from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'universities', views.UniversityViewSet)

urlpatterns = [
    path('', views.university, name='university'),
    path('api/',include(router.urls)),
 
]