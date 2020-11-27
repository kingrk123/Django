from django.shortcuts import render
from .models import SavingAccount
# Create your views here.
def ShowIndex(request):
    return render(request, 'index.html')


def registration(request):
    return render(request, "registration.html")


def saveAccount(request):
    account_no = request.POST.get("acno")
    name = request.POST.get("name")
    open_balance = request.POST.get("ob")
    upass = request.POST.get("password")

    sa = SavingAccount(Accno=account_no, Name=name, Balance=open_balance, password=upass)
    sa.save()
    return render(request, "index.html", {"message": "Account Created"})


def viewall(request):
    qs =SavingAccount.objects.all()
    return render(request, "viewall.html", {"data": qs})


def update(request):
    id = request.GET.get('update_idno')
    upd = SavingAccount.objects.get(Accno=id)
    return render(request, "update.html",  {"data": upd})