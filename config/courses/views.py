from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import DjangoModelPermissions

from config.settings import EMAIL_HOST_USER

from .models import *
from .serializers import *


class DaysViewSet(viewsets.ModelViewSet):
    """Viewset for Days"""
    queryset = Days.objects.all()
    serializer_class = DaysSerializer
    permission_classes = [DjangoModelPermissions]


class CategoryViewSet(viewsets.ModelViewSet):
    """Viewset for Category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [DjangoModelPermissions]


class CourseViewSet(viewsets.ModelViewSet):
    """Viewset for the Course"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissions]


class CourseGroupViewSet(viewsets.ModelViewSet):
    """Viewset for CourseGroups"""
    queryset = CourseGroup.objects.all()
    serializer_class = CourseGroupSerializer
    permission_classes = [DjangoModelPermissions]


class LessonViewSet(viewsets.ModelViewSet):
    """Viewset for the Lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [filters.SearchFilter]
    search_fields = ['topic']

    def get_queryset(self):
        search = self.request.query_params.get('topic')
        if search:
            return Lesson.objects.filter(topic=search)
        return Lesson.objects.all()


class LessonVideosViewSet(viewsets.ModelViewSet):
    """Viewset for Videos uploaded about Lesson"""
    queryset = LessonVideo.objects.all()
    serializer_class = LessonVideosSerializer
    permission_classes = [DjangoModelPermissions]


class TeacherViewSet(viewsets.ModelViewSet):
    """Viewsets for Teacher"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [DjangoModelPermissions]


class StudentViewSet(viewsets.ModelViewSet):
    """Viewsets for Student"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [DjangoModelPermissions]


class ReactionViewSet(viewsets.ModelViewSet):
    """ViewSet for Reaction"""
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    permission_classes = [DjangoModelPermissions]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Viewset for Comment"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [DjangoModelPermissions]

    def create(self, request, *args, **kwargs):
        lesson = request.data.get('lesson')
        student = request.data.get('student')
        content = request.data.get('content')

        if not lesson or not student:
            return Response({"error": "Lesson and student must be provided"})

        serializer = CommentSerializer(data={
            'lesson': lesson,
            'student': student,
            'content': content,
        })

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Comment created successfully", "data": serializer.data})
        return Response(serializer.errors)


class MessageApiView(APIView):
    """View for admins to send news to users about platform """
    def post(self, request: Request):
        serializers = MessageSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        
        send_mail(
            subject = serializers.validated_data.get("title"),
            message = serializers.validated_data.get("content"),
            from_email = EMAIL_HOST_USER,
            recipient_list = [user.email for user in User.objects.all() if user.email],
            fail_silently = False
        )
        return Response({"message": "Message sent successfully"})