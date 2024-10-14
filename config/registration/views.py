from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import Group
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class TeacherRegistrationViewSet(viewsets.ViewSet):
    """Viewset for registrating as a Teacher"""
    permission_classes = [AllowAny]

    def list(self, request):
        example_data = {
                "user": {
                    "username": "teacher_john",
                    "password": "securepassword123"
                },
                "experience": 5,
                "sphere_of_teaching": "Mathematics"
        }
        return Response({"example": example_data})

    def create(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            user = teacher.user
            teacher_group, created = Group.objects.get_or_create(name='Teachers')
            user.groups.add(teacher_group)

            return Response({'message': 'Teacher registered successfully!', 'data': serializer.data})
        return Response(serializer.errors)


class StudentRegistrationViewSet(viewsets.ViewSet):
    """Viewset for registrating as a Student"""
    permission_classes = [AllowAny]

    def list(self, request):
        example_data = {
    "user": {
        "username": "student_jane",
        "password": "securepassword123"
    },
    "birth_date": "2005-01-01",
    "phone_number": "+1234567890"
}
        return Response({"example": example_data})
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            user = student.user  

            student_group, created = Group.objects.get_or_create(name='Students')
            user.groups.add(student_group)

            return Response({'message': 'Student registered successfully!', 'data': serializer.data})
        return Response(serializer.errors)


class LoginViewSet(viewsets.ViewSet):
    """Viewsets for logging in"""
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                
                return Response({
                    'token': token.key,
                    'username': user.username,
                    'user_id': user.id,
                    'message':'success',
                },)
            else:
                return Response({'message': 'Invalid data'})
        
        return Response(serializer.errors, )