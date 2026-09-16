from django.shortcuts import render, get_object_or_404
from django.db import models

from .models import Laptop


def home(request):
    laptops = Laptop.objects.filter(
        is_available=True
    ).order_by('-created_at')[:4]

    return render(request, 'home.html', {
        'laptops': laptops
    })


def laptop_list(request):
    laptops = Laptop.objects.filter(
        is_available=True
    ).order_by('-created_at')

    search = request.GET.get('search', '')

    if search:
        laptops = laptops.filter(
            models.Q(brand__icontains=search) |
            models.Q(model_name__icontains=search) |
            models.Q(processor__icontains=search)
        )

    return render(request, 'laptops.html', {
        'laptops': laptops,
        'search': search,
    })


def laptop_detail(request, pk):
    laptop = get_object_or_404(
        Laptop,
        pk=pk,
        is_available=True
    )

    return render(request, 'laptop_detail.html', {
        'laptop': laptop
    })

def brands(request):
    return render(request, 'brands.html')

def services(request):
    return render(request, 'services.html')

def sell_laptop(request):
    return render(request, 'sell_laptop.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')