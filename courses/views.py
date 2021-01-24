from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, FormView
from django.views import View
from edu_site.tasks import do_mail_send

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
        email_subject = 'COURSESAPP :: Contact form message '
        email_body = "You have new message\n\n" \
                     "Sender name: %s \n" \
                     "Sender e-mail : %s \n\n" \
                     "Message: \n" \
                     "%s " % \
                     (form.cleaned_data['name'], form.cleaned_data['from_email'], form.cleaned_data['message'])
        from_email = form.cleaned_data['from_email']
        recipient_list = ['admin@example.com']

        do_mail_send.apply_async((email_subject, email_body, from_email, recipient_list),
                                 countdown=30)
        return HttpResponse('Your message was sent! Thanks')

    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = ContactForm()

        return render(request, template_name=self.template_name, context=context)
