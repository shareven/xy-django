from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("xyllll")

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    c=int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c=int(a)+int(b)
    d='{add_nums:'+str(c)+'}'
    return HttpResponse(d)

def template(request):

    return render(request,'index.html')