from django.contrib.auth.models import User, Group
from courses.models import Course, CourseModule, CourseCategory

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['course_title', 'description', 'start_date', 'end_date']  #'course__category',
#
#
# class CourseModuleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CourseModule
#         fields = ['category', 'module_title', 'start_date', 'end_date']
#
#
class CourseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['category_title']
