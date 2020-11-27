from django.http import HttpResponse

def wish(request):
    message="<h1>Goood  morning</h1>"
    return HttpResponse(message)
	