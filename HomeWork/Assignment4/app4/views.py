from django.shortcuts import render

# Create your views here.
def ShowIndex(request):
    return render(request, 'index.html')


def display(request):
    bsy = float(request.POST.get('bs'))
    da = float (0.2 * bsy)
    hra = float(0.4 * bsy)
    ts = float(bsy + da + hra)
    return render(request, 'index.html', {"data":ts})