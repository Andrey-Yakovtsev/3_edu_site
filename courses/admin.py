from django.contrib import admin
from .models import CourseCategory, Course, CourseModule
from accounts.models import Teacher

class MembershipInline(admin.TabularInline):
    model = Teacher.course.through
    def get_queryset(self, request):
        qs = super(MembershipInline, self).get_queryset()
        print(qs)
        return qs.prefetch_related('course__student')


class ModulesInline(admin.TabularInline):
    model = CourseModule


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ModulesInline,
               MembershipInline]

    def get_queryset(self, request):
        qs = super(CourseAdmin, self).get_queryset(request)
        return qs.prefetch_related('category')




@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
   list_display = ['title', 'start_date', 'end_date']