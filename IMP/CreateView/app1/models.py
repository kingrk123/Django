from django.db import models

class EmployeeModel(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=10,decimal_places=2)
    designation = models.CharField(max_length=30)
    contact = models.IntegerField(default=False)

