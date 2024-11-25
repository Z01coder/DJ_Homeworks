from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'myapp/page1.html')

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1><p>Это содержимое страницы Data.</p>")

def test_view(request):
    return HttpResponse("<h1>Страница Test</h1><p>Это содержимое страницы Test.</p>")

def page1(request):
    return render(request, 'myapp/page1.html')

def page2(request):
    return render(request, 'myapp/page2.html')

def page3(request):
    return render(request, 'myapp/page3.html')

def page4(request):
    return render(request, 'myapp/page4.html')

# Create your views here.
