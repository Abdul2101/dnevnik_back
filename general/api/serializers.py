from rest_framework import serializers
from general.models import CustomUser, StudentProfile, TeacherProfile, ParentProfile, Attendance, Grade, QuarterGrade, SchoolClass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'grade']

class TeacherProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeacherProfile
        fields = ['id', 'user', 'subject']

class ParentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    children = StudentProfileSerializer(many=True)

    class Meta:
        model = ParentProfile
        fields = ['id', 'user', 'children']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'student', 'teacher', 'subject', 'date', 'is_present']

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['id', 'student', 'teacher', 'subject', 'score', 'date']

class QuarterGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterGrade
        fields = ['id', 'student', 'teacher', 'subject', 'quarter', 'score', 'date']

class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'name']
