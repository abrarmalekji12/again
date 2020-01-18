"""again URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  path('',views.home,name='home'),
  path('logini',views.logini,name='As an Inspector'),
  path('loginm',views.loginm,name='As an Municipal Officer'),
 path('action/<slug:type>/',views.act,name="form1"),
  path('cudetails',views.cu_page,name="cudetails"),
   path('predetails',views.pre_page,name="predetails"),
    path('inscu',views.ins_cu,name="inscu"),
   path('inspre',views.ins_pre,name="inspre"),
   path('insadd',views.ins_add,name="insadd"),
   path('inhome',views.inhome,name="inhome"),
   path('road_det',views.road_det,name="road_det"),
   path('cons_add',views.cons_add,name="cons_add"),
   path('inconstruct/<int:t>/',views.inconstruct,name="inconstruct"),
   path('insfinal/',views.insfinal,name="insfinal"),
   path('insreq',views.insreq,name="insreq"),
   path('muhome',views.muhome,name='muhome'),
   path('muroad',views.muroad,name='muroad'),
   path('about',views.about,name="about"),
   path('contact',views.contact,name="contact"),
]