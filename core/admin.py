
from django.contrib import admin
from .models import Laptop


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):

    list_display = (
        'brand',
        'model_name',
        'processor',
        'ram',
        'storage',
        'price',
        'condition',
        'is_available',
    )

    list_filter = (
        'brand',
        'condition',
        'is_available',
    )

    search_fields = (
        'brand',
        'model_name',
        'processor',
    )

    ordering = (
        '-created_at',
    )
