from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import EmpoloyeeModel

class EmployeeList(ListView):
    model = EmpoloyeeModel
    template_name = "index.html"

class EmployeeDetails(DetailView):
    model = EmpoloyeeModel
    template_name = "showDetail.html"

class EmployeeCreate(CreateView):
    model = EmpoloyeeModel
    fields = "__all__"
    template_name = "create.html"
    success_url = '/main/'


def showIndex(request):
    return render(request,'base.html')