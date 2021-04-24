from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from courses.models import Course


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    course = models.ManyToManyField(Course, related_name='students', through='membership')

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    course = models.ManyToManyField(Course, related_name='teachers', through='Membership')

    def get_absolute_url(self):
        return reverse('teacher-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Membership(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='memberships')
    date_joined = models.DateField(auto_now_add=True)