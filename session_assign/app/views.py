from django.contrib import messages
from django.shortcuts import render, redirect
from .admin import SignInModel


def welcome(request):
    return render(request, 'welcome.html')


def signin(request):
    return render(request, 'signin.html')


def sign(request):
    uname = request.POST['uname']
    password = request.POST['password']
    try:
        SignInModel.objects.get(username=uname, password=password)
    except SignInModel.DoesNotExist:
        messages.error(request, 'Invalid UserName & Password')
        return redirect('/signin/')
    else:
        return render(request, 'showpage.html')


def logout(request):
    return signin(request)


def employee(request):
    return render(request, 'employee.html')


def faculty(request):
    return render(request, 'faculty.html')


def student(request):
    return render(request, 'student.html')