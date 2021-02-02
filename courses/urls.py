from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoriesListView, CourseListView, CourseDetailView, ModuleDetailView, CourseCreateView, \
    CourseUpdateView, CourseDeleteView, EmailContactsView, IndexView, \
    CourseDetailApiView, CategoryDetailApiView, CourseModuleApiView

app_name = 'courses'

router = DefaultRouter()
router.register('courses', CourseDetailApiView)
router.register('categories', CategoryDetailApiView)
router.register('modules', CourseModuleApiView)




urlpatterns = [
    # path('', CategoriesListView.as_view(), name='categories_list'),
    path('', IndexView.as_view(), name='index'),
    path('list/', CourseListView.as_view(), name='courses_list'),
    path('contacts/', EmailContactsView.as_view(), name='contacts'),
    path('courses/create/', CourseCreateView.as_view(), name='create_course'),
    path('course/<pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('course/<pk>/edit/', CourseUpdateView.as_view(), name='course_edit'),
    path('course/<pk>/delete/', CourseDeleteView.as_view(), name='course_delete'),
    path('course/module/<pk>/', ModuleDetailView.as_view(), name='module_detail'),
    path('api/', include(router.urls)),

]