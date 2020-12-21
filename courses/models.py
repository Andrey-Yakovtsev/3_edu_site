from django.db import models


class CourseCategory(models.Model):
    category_title = models.CharField(max_length=180, blank=False)
    class Meta:
        verbose_name_plural = 'Course categories'

    def __str__(self):
        return f'{self.category_title}'


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True)
    course_title = models.CharField(max_length=180, blank=False)
    description = models.TextField(max_length=1000, blank=False, null=False, help_text='Add course description')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.course_title}'


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='modules')
    module_title = models.CharField(max_length=180, blank=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.module_title}'
