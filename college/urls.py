from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'colleges', views.CollegeViewSet)
router.register(r'faculties', views.FacultyViewSet)

urlpatterns = [
    path('', views.college, name='college'),
    path('api/',include(router.urls)),
]