from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django.views import View
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from courses.serializers import UserSerializer, CourseSerializer, \
    CourseCategorySerializer, CourseModuleSerializer  # CourseModuleSerializer, CourseCategorySerializer

from .forms import ContactForm
from .models import CourseCategory, Course, CourseModule


class IndexView(View):
    template_name = 'courses/index.html'
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, template_name=self.template_name, context=context)


class CategoriesListView(ListView):
    model = CourseCategory


class CourseListView(ListView):
    model = Course


class CourseDetailView(DetailView):
    model = Course


class ModuleDetailView(DetailView):
    model = CourseModule


class CourseCreateView(CreateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses:courses_list')


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    success_url = reverse_lazy('courses:courses_list')


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:courses_list')


class EmailContactsView(FormView):
    template_name = 'courses/contacts.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.do_send_mail()
        return HttpResponse('Your message was sent! Thanks')


class CourseViewList(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailApiView(ModelViewSet):
    queryset = Course.objects.prefetch_related('modules')
    serializer_class = CourseSerializer


class CategoryDetailApiView(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer


class CourseModuleApiView(ModelViewSet):
    queryset = CourseModule.objects.all()
    serializer_class = CourseModuleSerializer

