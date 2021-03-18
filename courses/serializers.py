from courses.models import Course, CourseCategory, CourseModule

from rest_framework import serializers


class CourseCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseCategory
        fields = ['id', 'title']


class CourseModuleSerializer(serializers.HyperlinkedModelSerializer):
    course = serializers.HyperlinkedRelatedField(
        queryset=Course.objects.all(),
        view_name='courses:course-detail',
        allow_null=True,
    )

    class Meta:
        model = CourseModule
        fields = 'title', 'start_date', 'end_date', 'course_id', 'course'


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(
        queryset=CourseCategory.objects.all(),
        view_name='courses:coursecategory-detail',
        allow_null=True,
        )
    modules = serializers.HyperlinkedRelatedField(
        queryset=CourseModule.objects.all(),
        view_name='courses:coursemodule-detail',
        allow_null=True,
        many=True
    )

    class Meta:
        model = Course
        fields = 'id', 'title', 'description', 'start_date', 'end_date', 'category', 'category_id', 'modules'






