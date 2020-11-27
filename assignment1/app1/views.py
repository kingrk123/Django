from django.shortcuts import render

# Create your views here.
def Loginuser(request):
    return render(request,"index.html")


def LoginSuccessfull(request):
    uname = request.POST.get('username')
    upass = request.POST.get('password')
    if uname == "kiran" and upass == "123456":
        return render(request, "welcome.html")
    else:
        return render(request, "index.html", {'message': "Invalid Username & Password"})

def LogOut(request):
    return render(request, "index.html")


