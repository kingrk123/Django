from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.mail import send_mail
from project9 import settings as se
# Create your views here.
def home(request):
    return render(request, 'index.html')


def welcome(request):
    uname = request.POST.get('username')
    upass = request.POST.get('password')

    if uname == 'k' and upass == '1':
        subject = 'Check'
        mssg = 'This is check mail'
        from_mail = se.EMAIL_HOST_USER
        recipient_list = ["kiran.ranvirkar@gmail.com"]
        send_mail(subject, mssg, from_mail, recipient_list)
        return render(request, 'welcome.html')
    else:
        return render(request, 'index.html', {'message':'Invalid Usaername and Password'})


def logout(request):
    return render(request, "index.html")