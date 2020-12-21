from django.contrib import admin
from .models import Student, Teacher

@admin.register(Student)
class Student(admin.ModelAdmin):
    pass
    # list_display = ['id', 'first_name', 'last_name', 'date_joined']

@admin.register(Teacher)
class Teacher(admin.ModelAdmin):
    pass
    # list_display = ['id', 'first_name', 'last_name']