from django.shortcuts import render

# Create your views here.
def calc(request):
    return render(request, 'index.html')


def add(request):
    fno = int(request.POST.get('fnumber'))
    sno = int(request.POST.get('snumber'))
    sum1 = fno+sno
    return render(request, 'index.html', {'data': sum1})


def sub(request):
    fno = int(request.POST.get('fnumber'))
    sno = int(request.POST.get('snumber'))
    sub1 = fno - sno
    return render(request, 'index.html', {'data': sub1})


def mul(request):
    fno = int(request.POST.get('fnumber'))
    sno = int(request.POST.get('snumber'))
    mul1 = fno * sno
    return render(request, 'index.html', {'data': mul1})


def div(request):
    fno = int(request.POST.get('fnumber'))
    sno = int(request.POST.get('snumber'))
    div1 = fno / sno
    return render(request, 'index.html', {'data': div1})