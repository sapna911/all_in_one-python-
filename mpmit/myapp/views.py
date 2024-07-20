from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''def home(request):
    return HttpResponse('hello world')
'''


def contact(request):
    return HttpResponse('welcome to my website')

def fun(request):
    return HttpResponse('welcome to')
def home(request):
    return render(request,'contact.html',{'name':'sapna'})

def calci(request):
    return render(request,'calculator.html')

def add(request):
    a=int(request.POST['first no'])
    b=int(request.POST['second no'])
    c=a+b
    return render(request,'result.html',{'result':c})
