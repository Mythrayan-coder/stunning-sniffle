from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet
from . import views

router = DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.student_registration_form, name='registration_form'),
    
]