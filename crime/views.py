from django.shortcuts import render 
from . models import ComplaintReg
from . forms import ComplaintRegForms

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def service(request):
    return render(request,"service.html")

def public(request):
    return render(request,"public.html")

def news(request):
    return render(request,"news.html")

def contact(request):
    return render(request,"contact.html")

def gallary(request):
    return render(request,"gallary.html")

def complaint(request):
    if request.method == "POST":
        form = ComplaintRegForms(request.POST)
        form.is_valid()
        user=form.save()
        name =form.cleaned_data["name"]
        email =form.cleaned_data["email"]
        subject = "Registration Successful"
        message =f"""
                    Hello {name},
                    Your Complaint Is Successfully Compleated
                    Thank you
                """ 
        send_mail(subject,message,
                  settings.DEFAULT_FORM_EMAIL,[email],fail_silently=False)
        messages.success(request,"Registration is successful" )
        # name =request.POST.get("name")
        # phone =request.POST.get("phone")
        # complaint =request.POST.get("compalaint")

        # mydata = ComplaintReg(
        #     name=name,
        #     phone=phone,
        #     complaint =complaint
        # )
        # mydata.save()
        # print("saved")
    return render(request,"complaint.html")
def dashboard(request):
    data =ComplaintReg.objects.all()
    return render(request,"dashboard.html",{"data":data})
