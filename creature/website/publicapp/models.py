from django.db import models

# Create your models here.
class tbl_cont(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    msg=models.CharField(max_length=1000)
    reply=models.CharField(max_length=1000,default="Reply")
    replymessage=models.CharField(max_length=1000,default="-----")

class tbl_log(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
class tbl_upload(models.Model):
    image = models.ImageField(upload_to='images',verbose_name='file',null=True,blank=True)
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=1000)
    