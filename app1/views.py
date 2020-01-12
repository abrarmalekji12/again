from django.shortcuts import render
from django.http import HttpResponse
from numpy import array
# from sklearn.datasets import load_iris 

# Create your views here.
def home(request) :
    home=['find roads']
    details=['current details','history']
    login=['As an Inspector','As an Municipal Officer']
    return render(request,'abrar.html',{'home':home,'details':details,'login':login})
def logini(req) :
    return render(req,'login.html',{'ins':True})
def loginm(req) :
    return render(req,'login.html',{'ins':False})
def act(req) :
    if req.method == 'POST' :
      em=req.POST["email"]
      pas=req.POST["pass"]
      return HttpResponse("hey there "+em+" "+pas) 
    else :
      return HttpResponse("error with login")     
