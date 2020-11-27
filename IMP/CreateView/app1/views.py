from django.shortcuts import render
from django.views.generic import CreateView

from .models import EmployeeModel

class CreateEmployee(CreateView):
    model = EmployeeModel
    #fields = ["idno","name","salary","designation"]
    fields = "__all__"

    template_name = "index.html"
    success_url = '/save/'
