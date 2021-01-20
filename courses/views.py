from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.views import View
from redis import Redis
from rq import Queue

from .forms import ContactForm
from .models import CourseCategory, Course, CourseModule


queue = Queue(connection=Redis())



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
            email_subject = 'COURSESAPP :: Contact form message '
            email_body = "Yuo have new message\n\n" \
                         "Sender name: %s \n" \
                         "Sender e-mail : %s \n\n" \
                         "Message: \n" \
                         "%s " % \
                         (form.cleaned_data['name'], form.cleaned_data['from_email'], form.cleaned_data['message'])
            from_email = form.cleaned_data['from_email']
            recipient_list = ['admin@example.com']

            def do_mail_send():
                return send_mail(email_subject, email_body, from_email, recipient_list, fail_silently=False)
            job = queue.enqueue(do_mail_send)
            print(job)

            # send_mail(email_subject, email_body, from_email, recipient_list, fail_silently=False)

            return HttpResponse('Your message was sent! Thanks')
        return render(request, template_name=self.template_name, context=context)