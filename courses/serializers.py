from django.contrib.auth.models import User
from courses.models import Course, CourseCategory

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'title']
        view_name = 'category'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = 'id', 'title', 'description', 'start_date', 'end_date', 'category_id'  #, 'category_title'



# class CourseModuleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CourseModule
#         fields = ['category', 'title', 'start_date', 'end_date']



