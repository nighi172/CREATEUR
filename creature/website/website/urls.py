"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from publicapp.views import *
from adminapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"login/$",login,name="login"),
    url(r"home/$",home,name="home"),
    
    url(r"contact/$",contact,name="contact"),
    
    url(r"projects/$",projects,name="projects"),
    url(r"view/$",view,name="view"),
    url(r"reply/(?P<id>[0-9]+)",reply,name='reply'),
    url(r"index/$",index,name="index"),
    url(r"upload/$",upload,name="upload"),
    url(r"logout/$",logout,name="logout"),
    url(r"photo/$",photo,name="photo"),
    url(r"delete/(?P<id>[0-9]+)",delete,name='delete'),
    



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
