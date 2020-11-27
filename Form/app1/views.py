from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView

from app1.models import EmployeeModel
from .forms import EmployeeForm


class ShowIndex(FormView):
    template_name = "index.html"
    form_class = EmployeeForm

class SaveForm(CreateView):
    model = EmployeeModel
    fields = '__all__'
    template_name = "index.html"
    success_url = '/main/'

