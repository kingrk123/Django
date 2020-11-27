from django.shortcuts import render


def login(request):
    return render(request, 'login.html')


def welcome(request):
    uname = request.POST.get('username')
    upass = request.POST.get('password')
    if uname == 'abhishek' and upass == '123456':
        return render(request, 'welcome.html')
    else:
        return render(request, 'login.html', {'message': "Invalid Username and Password"})


def logout(request):
    return render(request, 'login.html')
