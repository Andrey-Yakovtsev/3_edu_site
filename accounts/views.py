from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Teacher, Student

class TeacherCreate(CreateView):
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('courses:index')


class StudentCreate(CreateView):
    model = Student
    fields = '__all__'
    success_url = reverse_lazy('courses:index')


class TeacherDetails(DetailView):
    model = Teacher


class StudentDetails(DetailView):
    model = Student


class TeacherList(ListView):
    model = Teacher


class StudentList(ListView):
    model = Student
