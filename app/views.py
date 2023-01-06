from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.

def home(request):
    return render(request,'home.html')

def registration(request):
    uf=UserForm()
    pf=ProfileForm()
    d={'uf':uf,'pf':pf}
    if request.method=='POST' and request.FILES:
        UD=UserForm(request.POST)
        PD=ProfileForm(request.POST,request.FILES)
        if UD.is_valid() and PD.is_valid():
            USO=UD.save(commit=False)
            pw=UD.cleaned_data['password']
            USO.set_password(pw)
            USO.save()

            PFO=PD.save(commit=False)
            PFO.user=USO
            PFO.save()
            send_mail('User registration','Registration is success full','abbubakar950@gmail.com',[USO.email],fail_silently=False)
            return HttpResponse('Registration is successfull')
    return render(request,'registration.html',d)