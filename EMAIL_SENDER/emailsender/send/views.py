from django.shortcuts import render
# from django.contrib import messages
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        sub=request.POST.get('subject')
        msg=request.POST.get('message')
        Temail=request.POST.get('Temail')
        Femail=request.POST.get('Femail')
        print(sub,msg,Temail)
        send_mail(sub,msg,Femail,[Temail])
        return HttpResponse('email send that !')
    return render(request,'home.html')