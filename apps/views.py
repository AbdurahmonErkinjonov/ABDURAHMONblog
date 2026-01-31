from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home_page(request):     
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        # ... POST so'rovni qayta ishlash ...
        return redirect('contact')
    
    # GET so'rovi uchun sahifani ko'rsatish
    return render(request, 'contact.html')