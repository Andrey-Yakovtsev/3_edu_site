import graphene
from graphene_django import DjangoObjectType

from courses.models import Course, CourseModule, CourseCategory
from accounts.models import Teacher, Student, Membership


class CourseCategoryType(DjangoObjectType):
    class Meta:
        model = CourseCategory
        fields = ("title",)


class CourseModuleType(DjangoObjectType):
    class Meta:
        model = CourseModule
        fields = ("title", "start_date", "end_date", "course")


class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ("title", "description", "start_date", "end_date", "category", "module", "teacher")


class MembershipType(DjangoObjectType):
    class Meta:
        model = Membership
        fields = ("course", "teacher", "student")


class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)
    all_categories = graphene.List(CourseCategoryType)
    all_modules = graphene.List(CourseModuleType)
    all_members = graphene.List(MembershipType)


    def resolve_all_courses(self, info):
        return Course.objects.prefetch_related().all()

    def resolve_all_categories(self, info):
        return CourseCategory.objects.all()

    def resolve_all_modules(self, info):
        return CourseModule.objects.all()

    def resolve_all_members(self, info):
        return Membership.objects.all()

schema = graphene.Schema(query=Query)