from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, StudentProfileViewSet, TeacherProfileViewSet, 
    ParentProfileViewSet, AttendanceViewSet, GradeViewSet, 
    QuarterGradeViewSet, SchoolClassViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'students', StudentProfileViewSet)
router.register(r'teachers', TeacherProfileViewSet)
router.register(r'parents', ParentProfileViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'quarter-grades', QuarterGradeViewSet)
router.register(r'school-classes', SchoolClassViewSet)

urlpatterns = router.urls
