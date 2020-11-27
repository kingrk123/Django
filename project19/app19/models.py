from django.db import models

class SavingAccount(models.Model):
    Accno = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=25)
    Balance = models.DecimalField(max_digits=10, decimal_places=2)
    password = models.CharField(max_length=30)
