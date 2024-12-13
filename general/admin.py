from django.contrib import admin
from .models import Grade, Attendance, QuarterGrade, SchoolClass, CustomUser, StudentProfile, TeacherProfile, ParentProfile


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject', 'score', 'date')  # Поля, отображаемые в списке
    list_filter = ('subject', 'date')  # Фильтры по предмету и дате
    search_fields = ('student__user__username', 'teacher__user__username', 'subject')  # Поля для поиска
    ordering = ('-date',)  # Сортировка


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'subject', 'date', 'is_present')  # Поля в списке
    list_filter = ('subject', 'date', 'is_present')  # Фильтры по предмету, дате и присутствию
    search_fields = ('student__user__username', 'teacher__user__username', 'subject')  # Поля для поиска
    ordering = ('-date',)  # Сортировка


@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Отображение имени класса
    search_fields = ('name',)  # Поля для поиска


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'email', 'is_active', 'is_staff')  # Поля в списке
    list_filter = ('role', 'is_active', 'is_staff')  # Фильтры по роли и статусу
    search_fields = ('username', 'email')  # Поля для поиска


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'grade')  # Поля в списке
    search_fields = ('user__username', 'grade__name')  # Поля для поиска
    list_filter = ('grade',)  # Фильтры по классу


@admin.register(TeacherProfile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject')  # Поля в списке
    search_fields = ('user__username', 'subject')  # Поля для поиска


@admin.register(ParentProfile)
class ParentProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)  # Поля в списке
    search_fields = ('user__username',)  # Поля для поиска
    filter_horizontal = ('children',)  # Удобный интерфейс для выбора детей



@admin.register(QuarterGrade)
class QuarterGradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'quarter', 'score', 'teacher', 'date')
    list_filter = ('quarter', 'subject', 'teacher')
    search_fields = ('student__user__username', 'subject')
