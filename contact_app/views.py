from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message has been received!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    return render(request, 'contact.html')
