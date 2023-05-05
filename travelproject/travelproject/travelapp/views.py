from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import team
# Create your views here.
def demo(request):
    # name='Basic operators'
    obj=Place.objects.all()
    obj2=team.objects.all()
    return render(request,"index.html",{'result':obj,'result2':obj2})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     x1=int(request.GET['num1'])
#     y1=int(request.GET['num2'])
#     res1=x1-y1
#     x2=int(request.GET['num1'])
#     y2=int(request.GET['num2'])
#     res2=x2*y2
#     x3=float(request.GET['num1'])
#     y3=float(request.GET['num2'])
#     res3=x3/y3
#     return render(request,"about.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})
def about(request):
    return render(request,'about.html')

def index(request):
    return render(request,'index.html')
