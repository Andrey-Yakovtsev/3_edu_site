from django.urls import path
from .views import CategoriesListView, CourseListView, CourseDetailView, ModuleDetailView, CourseCreateView, \
    CourseUpdateView, CourseDeleteView

app_name = 'courses'

urlpatterns = [
    # path('', CategoriesListView.as_view(), name='categories_list'),
    path('', CourseListView.as_view(), name='courses_list'),
    path('courses/create/', CourseCreateView.as_view(), name='create_course'),
    path('course/<pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/<pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('course/module/<pk>/', ModuleDetailView.as_view(), name='module_detail'),
]