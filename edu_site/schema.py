import graphene
from graphene_django import DjangoObjectType

from courses.models import Course, CourseModule, CourseCategory

class CourseType(DjangoObjectType):
    class Meta:
        model = Course
        fields = ("course_title", "description", "start_date", "end_date")

class CourseModuleType(DjangoObjectType):
    class Meta:
        model = CourseModule
        fields = ("module_title", "start_date", "end_date")


class CourseCategoryType(DjangoObjectType):
    class Meta:
        model = CourseCategory
        fields = ("category_title",)


class Query(graphene.ObjectType):
    all_courses = graphene.List(CourseType)

    def resolve_all_courses(self, info):
        # We can easily optimize query count in the resolve method
        return Course.objects.all()




schema = graphene.Schema(query=Query)