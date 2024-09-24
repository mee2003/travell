from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
# def index(request):
#     name=" india"
#     return render(request,"index.html",{'obj':name})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     res1=x-y
#     res2=x/y
#     res3= x*y
#
#     return render(request,"about.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})

def index(request):
    obj=place.objects.all()
    obj1 = team.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})

# def index(request):
#     obj1=team.objects.all()
#     return render(request,"index.html",{'result1':obj1})


def about(request):
    return render(request,"about.html")

def destinations(request):
    return render(request,"destinations.html")
#
def contact(request):
    return render(request,"contact.html")
#
def detail(request):
    return render(request,"detail.html")
def elements(request):
    return render(request,"elements.html")
def index1(request):
    return render(request,"index1.html")
def news(request):
    return render(request,"news.html")
#
# def thanks(request):
#     return HttpResponse("Thank You")