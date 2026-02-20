from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            
            # Send an email notification
            subject = f"New Contact Message from {name}"
            body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            
            try:
                send_mail(
                    subject,
                    body,
                    settings.EMAIL_HOST_USER,  # From email
                    [settings.EMAIL_HOST_USER, email],  # To email (receiving the notification)
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Error sending email: {e}")

            messages.success(request, 'Your message has been received!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'contact.html')
