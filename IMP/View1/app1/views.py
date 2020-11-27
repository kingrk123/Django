from django.shortcuts import render
from django.views.generic import View


def showOne(request):
    return render(request,"index.html")

def checkMethod(request):
    if request.method == "POST":
        x = request.POST.get("p1")
        return render(request,"index.html",{"message":"Clicked on POST Button : "+x})
    else:
        y = request.GET.get("p1")
        return render(request,"index.html",{"message":"Get Button is Clicked : "+y})


class Check(View):
    def post(self,request,*args,**kwargs):
        return render(request,"index1.html",{"message":"POST CLICKED"})

    def get(self,request,*args,**kwargs):
        return render(request,"index1.html",{"message":"GET CLICKED"})









