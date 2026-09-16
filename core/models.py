
from django.db import models


class Laptop(models.Model):

    CONDITION_CHOICES = [
        ('Refurbished', 'Refurbished'),
        ('Used', 'Used'),
    ]

    brand = models.CharField(max_length=50)

    model_name = models.CharField(max_length=150)

    processor = models.CharField(max_length=100)

    ram = models.CharField(max_length=50)

    storage = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    condition = models.CharField(
        max_length=20,
        choices=CONDITION_CHOICES,
        default='Refurbished'
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to='laptops/',
        blank=True,
        null=True
    )

    warranty = models.CharField(
        max_length=100,
        blank=True
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.brand} {self.model_name}"

