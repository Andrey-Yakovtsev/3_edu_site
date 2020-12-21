from django.contrib import admin
from .models import CourseCategory, Course, CourseModule

# class CourseModuleInline(admin.StackedInline):
#     model = CourseModule

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_title', ]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'start_date', 'end_date']

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
   list_display = ['module_title', 'start_date', 'end_date']