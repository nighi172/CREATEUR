from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings



# Create your views here.


def login(request):
    msg=""
    
    if request.method=="POST":
        a=request.POST.get("t1")
        b=request.POST.get("t2")
        if tbl_log.objects.filter(username=a,password=b):
            data=tbl_log.objects.get(username=a,password=b)
            aid=data.id
            request.session['adminid']=aid
            return HttpResponseRedirect(reverse('index'))
        else:
            msg="invalid credentials"
    return render(request,"publicapp/login.html",{"msg":msg})

def home(request):
    data1=tbl_upload.objects.all()

    return render(request,"publicapp/publicapp_layout.html",{"data1":data1})



def contact(request):
    message=""
    data1=tbl_upload.objects.all()
    if request.method=="POST":
        a=request.POST.get("tb1")
        b=request.POST.get("tb2")
        c=request.POST.get("tb3")
        data=tbl_cont.objects.create(name=a,email=b,msg=c)
        
        message="SEND SUCCESS"
    return render(request,"publicapp/publicapp_layout.html",{"message":message,"data1":data1})



def projects(request):
    data1=tbl_upload.objects.all()
    return render(request,"publicapp/publicapp_layout.html",{"data1":data1})



def logout(request):
    data=request.session.delete()
    return HttpResponseRedirect(reverse('home'))


