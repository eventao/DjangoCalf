#from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
    # return HttpResponse("Hello world!")

def about(request):
    context = {}
    context['title'] = '关于我们！'
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    context['title'] = '联系我们！'
    return render(request, 'contact.html', context)

