from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username}'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=True, null=True, default=True)

    def get_absolute_url(self):
        return reverse('teacher-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.user.username}'
