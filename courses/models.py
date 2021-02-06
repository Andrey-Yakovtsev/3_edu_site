from django.db import models



class CourseCategory(models.Model):
    title = models.CharField(max_length=180, blank=False)
    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return f'{self.title}'


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, related_name='courses')
    title = models.CharField(max_length=180, blank=False)
    description = models.TextField(max_length=1000, blank=False, null=False, help_text='Add course description')
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}'


class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, related_name='modules')
    title = models.CharField(max_length=180, blank=False)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    class Meta:
        verbose_name = 'Module'
        verbose_name_plural = 'Modules'

    def __str__(self):
        return f'{self.title}'
