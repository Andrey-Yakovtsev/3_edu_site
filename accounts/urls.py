from django.urls import path

from .views import StudentDetails, TeacherDetails, StudentList, TeacherList, user_login, register_student, register_teacher


app_name = 'accounts'


urlpatterns = [
path('teacher_create/', register_teacher, name='teacher_create'),
path('student_create/', register_student, name='student_create'),
path('students/', StudentList.as_view(), name='students_list'),
path('teachers/', TeacherList.as_view(), name='teachers_list'),
path('student/<pk>/', StudentDetails.as_view(), name='student_detail'),
path('teacher/<pk>/', TeacherDetails.as_view(), name='teacher_detail'),
path('login/', user_login, name='login'),

# path('course/module/<pk>/', ModuleDetailView.as_view(), name='module_detail'),

    ]