from django.contrib.auth.models import User

from rest_framework import serializers

from accounts.models import Student, Teacher

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(
        queryset=Student.objects.all(),
        view_name='accounts:student_list',
        allow_null=True,
        )
    teacher = serializers.HyperlinkedRelatedField(
        queryset=Teacher.objects.all(),
        view_name='accounts:teacher_list',
        allow_null=True,
        many=True
    )

    class Meta:
        model = User
        fields = '__all__'


