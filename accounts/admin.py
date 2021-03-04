from django.contrib import admin

from .models import Student, Teacher


class MembershipInline(admin.TabularInline):
    model = Teacher.course.through
    def get_queryset(self, request):
        qs = super(MembershipInline, self).get_queryset(request)
        # print(qs.values())
        # print(qs.prefetch_related('course').values())
        return qs.prefetch_related('course')



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        return qs.prefetch_related('user')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TeacherAdmin, self).get_queryset(request)
        return qs.prefetch_related('user')
    inlines = [
        MembershipInline
    ]
