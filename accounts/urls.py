from django.urls import path

from .views import TeacherCreate, StudentCreate, StudentDetails, TeacherDetails, StudentList, TeacherList


app_name = 'accounts'


urlpatterns = [
path('teacher_register/', TeacherCreate.as_view(), name='teacher_create'),
path('student_register/', StudentCreate.as_view(), name='student_create'),
path('students/', StudentList.as_view(), name='students_list'),
path('teachers/', TeacherList.as_view(), name='teachers_list'),
path('student/<pk>/', StudentDetails.as_view(), name='student_detail'),
path('teacher/<pk>/', TeacherDetails.as_view(), name='teacher_detail'),

# path('course/module/<pk>/', ModuleDetailView.as_view(), name='module_detail'),

    ]