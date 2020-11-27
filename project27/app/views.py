from django.shortcuts import render,redirect

# Create your views here.
from app.models import EmployeeModel
from .forms import EmployeeForm
from django.contrib import messages


def ShowIndex(request):
    ef = EmployeeForm()
    return render(request, "index.html", {"form": ef})


def SaveForm(request):
    id = request.POST.get('F_idno')
    na = request.POST.get('F_name')
    sal = request.POST.get('F_salary')
    EmployeeModel(idno=id, name=na, salary=sal).save()
    messages.success(request,'Sucessfull Save')
    return redirect('main')