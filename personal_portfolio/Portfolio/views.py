from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail
from .forms import ContactForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            send_mail(
                subject=f"New Message from {name}",
                message=message,
                from_email='santhoshmanoharan.edu@gmail.com',
                recipient_list=[email],  # Replace with your email address
                fail_silently=False,
            )
            messages.success(request, 'Email sent successfully!')
            # return redirect('home')  # Redirect to home page to display the message
    else:
        form = ContactForm()

    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'form': form})

def ml_project(request):
    return (render(request,'portfolio/ml_project.html'))

