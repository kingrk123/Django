from django import forms
from .models import EmployeeModel


class EmployeeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = EmployeeModel
        fields = "__all__"

