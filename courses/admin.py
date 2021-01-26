from django.contrib import admin
from .models import CourseCategory, Course, CourseModule

# class CourseModuleInline(admin.StackedInline):
#     model = CourseModule

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
   list_display = ['title', 'start_date', 'end_date']