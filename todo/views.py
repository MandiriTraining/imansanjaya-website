from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Belajar Django Luuur")
    return render(request, 'todo/index.html')
