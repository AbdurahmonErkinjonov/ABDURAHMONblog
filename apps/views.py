from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import ContactMessage

class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['home', 'contact']

    def location(self, item):
        return reverse(item)

def home_page(request):     
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        # ... POST so'rovni qayta ishlash ...
        return redirect('contact')
    
    # GET so'rovi uchun sahifani ko'rsatish
    return render(request, 'contact.html')