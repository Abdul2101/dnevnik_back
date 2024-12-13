from rest_framework import viewsets
from general.models import CustomUser, StudentProfile, TeacherProfile, ParentProfile, Attendance, Grade, QuarterGrade, SchoolClass
from .serializers import (
    UserSerializer, StudentProfileSerializer, TeacherProfileSerializer, 
    ParentProfileSerializer, AttendanceSerializer, GradeSerializer, 
    QuarterGradeSerializer, SchoolClassSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherProfileSerializer

class ParentProfileViewSet(viewsets.ModelViewSet):
    queryset = ParentProfile.objects.all()
    serializer_class = ParentProfileSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class QuarterGradeViewSet(viewsets.ModelViewSet):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterGradeSerializer

class SchoolClassViewSet(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer
