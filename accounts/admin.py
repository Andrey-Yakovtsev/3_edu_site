from django.contrib import admin
from django.forms import BaseInlineFormSet

from .models import Student, Teacher

class MembershipInlineFormSet(BaseInlineFormSet):

    def get_queryset(self):
        qs = super(MembershipInlineFormSet, self).get_queryset()
        # return qs.prefetch_related('course')
        return qs.filter()

class MembershipInline(admin.TabularInline):
    # model = Teacher.course.through
    model = Teacher.course.through
    formset = MembershipInlineFormSet
    extra = 0



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(StudentAdmin, self).get_queryset(request)
        return qs.prefetch_related('user')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(TeacherAdmin, self).get_queryset(request)
        # return qs.prefetch_related('user')
        return qs.prefetch_related('memberships')
    inlines = [
        MembershipInline
    ]
