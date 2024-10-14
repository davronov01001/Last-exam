from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherRegistrationViewSet, StudentRegistrationViewSet, LoginViewSet

router = DefaultRouter()
router.register(r'register/teacher', TeacherRegistrationViewSet, basename='teacher_register')
router.register(r'register/student', StudentRegistrationViewSet, basename='student_register')
router.register(r'login', LoginViewSet, basename='login')

urlpatterns = router.urls