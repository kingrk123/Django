from django.shortcuts import render

# Create your views here.
def inputfield(request):
    return render(request, 'index.html')


def display(request):
    subj1 = int(request.POST.get('sub1'))
    subj2 = int(request.POST.get('sub2'))
    subj3 = int(request.POST.get('sub3'))
    total = (subj1 + subj2 + subj3)
    avg = int(total/3)
    return render(request, 'index.html', {'marks': {'to': total, 'av': avg, 'subject1': subj1, 'subject2': subj2, 'subject3': subj3}})