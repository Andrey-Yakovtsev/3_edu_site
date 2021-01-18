from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views import View

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


class EmailContactsView(View):
    template_name = 'courses/contacts.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context.update(csrf(request))    # Обязательно добавьте в шаблон защитный токен
        context['form'] = ContactForm()

        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        context = {}
        form = ContactForm(request.POST)
        if form.is_valid():
            email_subject = 'COURSESAPP :: Сообщение через контактную форму '
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "E-mail отправителя: %s \n\n" \
                         "Сообщение: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['from_email'], form.cleaned_data['message'])
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['andrey@tri-sport.ru'], fail_silently=False)
            return HttpResponse('Your message was sent! Thanks')
        return render(request, template_name=self.template_name, context=context)