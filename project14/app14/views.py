from django.shortcuts import render

def show(request):
    return render(request, 'index.html')

def welcome(request):
    fname = request.POST.get('firstname')
    lname = request.POST.get('lastname')
    return render(request, 'index.html', {'message': {'f': fname, 'l': lname}})


