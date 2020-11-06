from django.shortcuts import render
from publicapp.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def view(request):
    admin=request.session["adminid"]
    data=tbl_cont.objects.all()
    return render(request,"adminapp/view.html",{"data":data})


def reply(request,id):
    data=tbl_cont.objects.get(id=id)
    admin1=request.session['adminid']
    if request.method=='POST':
        if data.reply=='Reply':
            a=request.POST.get("tb3")
            subject='Reply from CREATEUR'
            message=a
            email_from=settings.EMAIL_HOST_USER
            recipientlist=[data.email,]
            send_mail(subject,message,email_from,recipientlist,fail_silently=True)

            data.reply="Replied"
            data.replymessage=a
            data.save()
            return HttpResponseRedirect(reverse('view'))
    return render(request,"adminapp/reply.html",{"data":data})

def index(request):
    admin=request.session["adminid"]
    return render(request,"adminapp/index.html",{})

def upload(request):
    msg=""
    if request.method=="POST":
        a=request.POST.get('t1')
        b=request.POST.get('t2')
        imag=request.FILES['img']
        data=tbl_upload.objects.create(name=a,address=b,image=imag)
        msg="upload success"
    
    return render(request,"adminapp/upload.html",{"msg":msg})

def photo(request):
    admin=request.session['adminid']
    data=tbl_upload.objects.all()
    
    return render(request,"adminapp/view_photo.html",{"data":data})

def delete(request,id):
    data=tbl_upload.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('photo'))





