from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

def home(request):
    return render(request , 'core/index.html' )

def about(request):
    skills = ['Python', 'Django', 'JavaScript', 'HTML', 'CSS', 'Bootstrap', 'Git', 'REST APIs', 'PostgreSQL', 'React']
    return render(request, 'core/about.html', {'skills': skills})
def services(request):
    return render(request , 'core/services.html' )

def projects(request):
    return render(request , 'core/projects.html' )

def contact(request):
    if request.method == 'POST':
        name    = request.POST.get('name')
        email   = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject=f"Portfolio Contact: {subject}",
            message=f"From: {name} <{email}>\n\n{message}",
            from_email=email,
            recipient_list=['your@gmail.com'],  
        )
        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'core/contact.html')