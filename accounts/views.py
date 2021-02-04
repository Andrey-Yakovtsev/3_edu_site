import requests
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from rest_framework_simplejwt import tokens

from .forms import LoginForm, UserRegistrationForm, UpdateTokenForm
from .models import Teacher, Student



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                            username=cd['username'],
                            password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/templates/registration/login.html', {'form': form})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
    else:
        return render(request, 'accounts/logout.html')

def register_teacher(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Teacher.objects.create(user=new_user)
            return render(request,
                          'accounts/signup_complete.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'accounts/teacher_form.html',
                  {'user_form': user_form})


def register_student(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()
            Student.objects.create(user=new_user)
            return render(request,
                          'accounts/signup_complete.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'accounts/student_form.html',
                  {'user_form': user_form})

class TeacherDetails(DetailView):
    model = Teacher


class StudentDetails(DetailView):
    model = Student


class TeacherList(ListView):
    model = Teacher


class StudentList(ListView):
    model = Student


def get_user_token(request):
    url = 'http://127.0.0.1:8000/api/token/'
    headers = {
        'Content-Type': 'application/json'
    }
    if request.method == 'POST':
        get_token_form = LoginForm(request.POST)
        refresh_token_form = UpdateTokenForm(request.POST)

        if get_token_form.is_valid():
            response = requests.post(url, data = {
                'username': get_token_form.cleaned_data['username'],
                'password': get_token_form.cleaned_data['password']})

            return render(request,
                          'accounts/tokenize_result.html',
                          {'token': response.json(),
                           'form': refresh_token_form})
    else:
        get_token_form = LoginForm()

    return render(request,
                  'accounts/tokenize.html',
                  {'form': get_token_form})
