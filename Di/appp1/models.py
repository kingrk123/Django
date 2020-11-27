from django.db import models

# Create your models here.
class SavingAccount(models.Model):
    Accno = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=10)
    Balance = models.DecimalField(max_digits=10,decimal_places=2)
    Password=models.CharField(max_length=30)

