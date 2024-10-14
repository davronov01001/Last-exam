from rest_framework.routers import DefaultRouter
from .views import *
from django.urls import *

router = DefaultRouter()
router.register(r'days', DaysViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'course-groups', CourseGroupViewSet)
router.register(r'lessons', LessonViewSet, basename='lessons')
router.register(r'lesson-videos', LessonVideosViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)
router.register(r'reactions', ReactionViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls 
