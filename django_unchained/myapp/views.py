from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, Django!")

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1><p>Это содержимое страницы Data.</p>")

def test_view(request):
    return HttpResponse("<h1>Страница Test</h1><p>Это содержимое страницы Test.</p>")

# Create your views here.
