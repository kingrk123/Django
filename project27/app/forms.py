from django import forms

class EmployeeForm(forms.Form):
    F_idno = forms.IntegerField()
    F_name = forms.CharField()
    F_salary = forms.FloatField()

