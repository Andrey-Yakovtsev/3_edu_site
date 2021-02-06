from django.contrib import admin
from .models import CourseCategory, Course, CourseModule
from accounts.models import Teacher

class MembershipInline(admin.TabularInline):
    model = Teacher.course.through


class ModulesInline(admin.TabularInline):
    model = CourseModule

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModulesInline,
               MembershipInline]



@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
   list_display = ['title', 'start_date', 'end_date']