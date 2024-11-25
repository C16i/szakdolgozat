

from django.http import HttpResponse

def elso(request):
    return HttpResponse("Szia!")

def home(request):
    return HttpResponse("<h1> Homepage </h1>")