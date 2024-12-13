from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class Attendance(models.Model):
    student = models.ForeignKey(
        'StudentProfile',
        on_delete=models.CASCADE,
        related_name='attendance_records',
        verbose_name=_('Ученик')
    )
    teacher = models.ForeignKey(
        'TeacherProfile',
        on_delete=models.CASCADE,
        related_name='attendance_records',
        verbose_name=_('Учитель')
    )
    subject = models.CharField(
        max_length=100,
        verbose_name=_('Предмет')
    )
    date = models.DateField(verbose_name=_('Дата'))
    is_present = models.BooleanField(default=True, verbose_name=_('Присутствие'))

    class Meta:
        verbose_name = _('Посещаемость')
        verbose_name_plural = _('Посещаемость')
        ordering = ['-date']  # Сортировка по дате

    def __str__(self):
        status = _('Присутствовал') if self.is_present else _('Отсутствовал')
        return f"{self.student.user.get_full_name()} - {self.subject}: {status} ({self.date})"



class Grade(models.Model):
    student = models.ForeignKey(
        'StudentProfile',
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name=_('Ученик')
    )
    teacher = models.ForeignKey(
        'TeacherProfile',
        on_delete=models.CASCADE,
        related_name='grades',
        verbose_name=_('Учитель')
    )
    subject = models.CharField(
        max_length=100,
        verbose_name=_('Предмет')
    )
    score = models.PositiveIntegerField(verbose_name=_('Оценка'))  # Например, 1-5 или 1-10
    date = models.DateField(auto_now_add=True, verbose_name=_('Дата'))

    class Meta:
        verbose_name = _('Оценка')
        verbose_name_plural = _('Оценки')
        ordering = ['-date']  # Сортировка по дате

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.subject}: {self.score}"


class SchoolClass(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name=_('Название класса'))

    class Meta:
        verbose_name = _('Школьный класс')
        verbose_name_plural = _('Школьные классы')

    def __str__(self):
        return self.name
class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = 'student', _('Ученик')
        TEACHER = 'teacher', _('Учитель')
        PARENT = 'parent', _('Родитель')

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # уникальное имя для обратной связи
        blank=True,
        verbose_name=_('Группы'),
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # уникальное имя для обратной связи
        blank=True,
        verbose_name=_('Права пользователя'),
    )

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if is_new:
            if self.role == self.Role.STUDENT and not hasattr(self, 'student_profile'):
                StudentProfile.objects.create(user=self)
            elif self.role == self.Role.TEACHER and not hasattr(self, 'teacher_profile'):
                TeacherProfile.objects.create(user=self)
            elif self.role == self.Role.PARENT and not hasattr(self, 'parent_profile'):
                ParentProfile.objects.create(user=self)
            else:
                raise ValidationError(_("Необходимо создать профиль для этого типа пользователя."))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"








class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class StudentProfile(UserProfile):
    grade = models.ForeignKey(SchoolClass, on_delete=models.SET_NULL, null=True, verbose_name=_('Класс'))

    class Meta:
        verbose_name = _('Профиль ученика')
        verbose_name_plural = _('Профили учеников')

    def __str__(self):
        return f"Профиль ученика: {self.user.username}"


class TeacherProfile(UserProfile):
    subject = models.CharField(max_length=100, verbose_name=_('Предмет'))

    class Meta:
        verbose_name = _('Профиль учителя')
        verbose_name_plural = _('Профили учителей')

    def __str__(self):
        return f"Профиль учителя: {self.user.username}"


class ParentProfile(UserProfile):
    children = models.ManyToManyField(StudentProfile, related_name='parents', verbose_name=_('Дети'))

    class Meta:
        verbose_name = _('Профиль родителя')
        verbose_name_plural = _('Профили родителей')

    def __str__(self):
        return f"Профиль родителя: {self.user.username}"
    

class QuarterGrade(models.Model):
    student = models.ForeignKey(
        'StudentProfile',
        on_delete=models.CASCADE,
        related_name='quarter_grades',
        verbose_name=_('Ученик')
    )
    teacher = models.ForeignKey(
        'TeacherProfile',
        on_delete=models.CASCADE,
        related_name='quarter_grades',
        verbose_name=_('Учитель')
    )
    subject = models.CharField(
        max_length=100,
        verbose_name=_('Предмет')
    )
    quarter = models.PositiveIntegerField(
        choices=[(1, _('1 четверть')), (2, _('2 четверть')), (3, _('3 четверть')), (4, _('4 четверть'))],
        verbose_name=_('Четверть')
    )
    score = models.PositiveIntegerField(verbose_name=_('Оценка'))  # Оценка за четверть
    date = models.DateField(auto_now_add=True, verbose_name=_('Дата оценки'))

    class Meta:
        verbose_name = _('Четвертная оценка')
        verbose_name_plural = _('Четвертные оценки')
        ordering = ['student', 'subject', 'quarter']  # Сортировка по студенту, предмету и четверти

    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.subject} ({self.quarter} четверть): {self.score}"

