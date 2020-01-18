from django.shortcuts import render,redirect
from django.http import HttpResponse
# from django.contrib.auth.models import auth,User
from numpy import array
from app1.models import MuOff,InsOff,Construction,Road,Schedule,history
# from sklearn.datasets import load_iris 
'''
mode 0 home
     1 current
     2 previous
     :	#353A40
'''
# Create your views here.
class MyUser :
    log:bool
    isIns:bool
    ins:InsOff
    muf:MuOff
    road:Road
    def __init__(self):
        self.log=False
        self.isIns=True
        self.road=None
        self.ins=None
        self.muf=None
    def register(self,t,ob) :
        self.log=True
        self.isIns=t
        if t is True:
          self.ins=ob
        else :
          self.muf=ob    
    def logout(self) :
         self.log=False
         self.ins=None
         self.muf=None      
    def isLog(self) :
        return self.log
    def isInspector(self) :
        return self.isIns    
user=MyUser()
def home(request) :
    user.logout()
    return render(request,'abrar.html',{'mode':0})
def logini(req) :
    user.logout()
    return render(req,'login.html',{'ins':True,'act':'Inspector'})
def loginm(req) :
    user.logout()
    return render(req,'login.html',{'ins':False,'act':'Municipal'})
def act(req,type) :
    if req.method == 'POST' :
      em=req.POST["email"]
      pas=req.POST["pass"]
      if type=='Inspector' :
       if InsOff.objects.filter(email=em,passw=pas).exists() :
        i=InsOff.objects.get(email=em,passw=pas)
        user.register(True,i)       
        sc=Road.objects.all() 
        return render(req,'Inspage.html',{'mode':0,'rd':sc,'note':(sc.count()!=0)})
       else :
        return redirect('/logini')
      else :
       if MuOff.objects.filter(email=em,passw=pas).exists() :
        i=MuOff.objects.get(email=em,passw=pas)
        user.register(False,i)   
        return render(req,'Mupage.html',{'mode':0})
       else :
        return redirect('/loginm')
    else : 
       return redirect('/')
def cu_page(req) :
    sc=Schedule.objects.all().order_by('construction__road__city')
    return render(req,'abrar.html',{'cu':sc,'mode':1,'note':(sc.count()!=0)})     
def pre_page(req) :
    sc=history.objects.all().order_by('construction__road__city')
    return render(req,'abrar.html',{'cu':sc,'mode':2,'note':(sc.count()!=0)}) 
def ins_cu(req) :
    sc=Schedule.objects.all()
    return render(req,'Inspage.html',{'cu':sc,'mode':1,'note':(sc.count()!=0)}) 
def ins_pre(req) :
    sc=history.objects.all()
    return render(req,'Inspage.html',{'cu':sc,'mode':2,'note':(sc.count()!=0)})
def ins_add(req) :
  if user.isLog() :  
    return render(req,'Inspage.html',{'mode':3})
def inhome(req) :
    if user.isIns and user.log :
        sc=Road.objects.all() 
        return render(req,'Inspage.html',{'mode':0,'rd':sc,'note':(sc.count()!=0)})
    else :
        return redirect('/')     
def road_det(req) :
    if user.isIns and user.log :
        sc=Road.objects.all() 
        return render(req,'Inspage.html',{'mode':4,'rd':sc,'note':(sc.count()!=0)}) 
    else :
        return redirect('/')    
def cons_add(req) :
    if req.method == 'POST' :
          r=Road(name=req.POST['road_name'],area=req.POST['area'],city=req.POST['city'],pin=req.POST['pin'],length=req.POST['length'],lane=req.POST['width'])             
          #,image=req.POST['image']
          r.save()
          if user.isIns and user.log :
           sc=Road.objects.all() 
           return render(req,'Inspage.html',{'mode':4,'rd':sc,'note':(sc.count()!=0)}) 
    else :
        return redirect('/')
def inconstruct(req,t) :
    if req.method=='POST' :
        sc=Road.objects.get(id=t)
        user.road=sc
        return render(req,'Inspage.html',{'mode':-1,'sr':sc}) 
    else :
      return redirect('/') 
def insfinal(req) :
    if req.method=='POST' and user.isInspector() :
        # fs=req.FILES['image']
        c=Construction(road=user.road,inspector=user.ins,status=1,fund=req.POST['fund'])
        c.save()
        return HttpResponse("Response updated")
    else :
      return redirect('/')                         
def insreq(req) :
    if user.log and user.isIns :
     c=Construction.objects.filter(status__in=[1,2])
     return render(req,'Inspage.html',{'mode':-2,'co':c,'note':(c.count()!=0)})
    else :
      return redirect('/')            
def muhome(req) :
    return render(req,'Mupage.html',{'mode':0}) 
def about(req) :
    return render(req,'aboutus.html')
def contact(req) :
    return render(req,'form23.html')
def muroad(req) :
    if (not user.isIns) and user.log :
        sc=Road.objects.all() 
        return render(req,'Mupage.html',{'mode':4,'rd':sc,'note':(sc.count()!=0)}) 
    else :
        return redirect('/')  