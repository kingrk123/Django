from django.shortcuts import render

def show(request):
    d={"id":123456,"name":"KINGRK","mob":9623240111}
    return render(request,"abc.html",d)
