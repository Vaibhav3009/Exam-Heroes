from django.shortcuts import render,redirect
from django.conf import settings 
from django.core.mail import send_mail 
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'main/index.html')



def contact(request):

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        
        subject = 'Greetings from ExamHeroes'
        message1 = f'Hi {name}, thank you for contacting us. We will get back to you soon.\n\nRegards,\nExamHeroes'
        print(message1)
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [email, ] 
        send_mail( subject, message1, email_from, recipient_list ) 
        messages.success(request, 'Form submission successful')

        return redirect('/#contact')