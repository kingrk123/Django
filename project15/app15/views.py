from django.shortcuts import render

# Create your views here.
def ShowIndex(request):
    return render(request, 'index.html')


def display(request):
    return render(request, 'view.html')