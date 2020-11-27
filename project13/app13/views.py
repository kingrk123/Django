from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'index.html')


def welcome(request):
    uname = request.POST.get('username')
    upass = request.POST.get('password')
    if uname == 'kiran' and upass == '123456':
        pass
    else:
        return render(request, 'index.html', {'message': "Invalid Username & Password"})
