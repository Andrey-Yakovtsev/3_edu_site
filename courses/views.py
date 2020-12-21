from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import CourseCategory, Course, CourseModule


class CategoriesList(ListView):
    model = CourseCategory


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class ModuleDetailView(DetailView):
    model = CourseModule

