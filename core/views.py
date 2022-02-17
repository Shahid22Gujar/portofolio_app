from django.shortcuts import render
from core.email import send_email
from .models import User
from django.contrib import messages
# from simple_colors import *


# Create your views here.
def home(request):
    context = {'home':'active'}
    return render(request,'core/home.html',context)
def contact(request):
    if request.method == "POST":
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        textfield=request.POST.get("textfield")
        contact=User(fname=fname,lname=lname,email=email,textfield=textfield)
        contact.save()
        message=f"Name:{fname} {lname} \n From :{email} \n Text: {textfield}"
        send_email(email,message)
        messages.success(request,  'Form has been submitted.')
        
    context = {'contact':'active'}
    return render(request,'core/contact.html',context)


