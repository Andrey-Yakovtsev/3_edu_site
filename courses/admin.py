from django.contrib import admin
from .models import CourseCategory, Course, CourseModule

# class CourseModuleInline(admin.StackedInline):
#     model = CourseModule

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['description', 'start_date', 'end_date']

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    pass