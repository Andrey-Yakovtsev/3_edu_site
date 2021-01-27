from django.contrib.auth.models import User
from courses.models import Course, CourseCategory

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class CourseCategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CourseCategory
        fields = ['id', 'title']
        view_name = 'category'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    # category = serializers.HyperlinkedIdentityField(view_name='category')
    class Meta:
        model = Course
        fields = 'id', 'title', 'description', 'start_date', 'end_date', 'category'

    category = CourseCategorySerializer()
    # category = serializers.PrimaryKeyRelatedField(many=False, queryset=CourseCategory.objects.all())


# class CourseModuleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CourseModule
#         fields = ['category', 'title', 'start_date', 'end_date']



