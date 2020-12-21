from django.urls import path
from .views import CategoriesList, CourseListView, CourseDetailView, ModuleDetailView


app_name = 'courses'

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('courses/', CourseListView.as_view(), name='courses_list'),
    path('course/<pk>', CourseDetailView.as_view(), name='course_detail'),
    path('course/module/<pk>', ModuleDetailView.as_view(), name='module_detail'),
]