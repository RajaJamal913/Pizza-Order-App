from django.db import models
from django.utils import timezone

# Pizza model to store pizza details
from django.db import models

class Pizza(models.Model):
    PIZZA_TYPE_CHOICES = [
        ('veg', 'Vegetarian'),
        ('non_veg', 'Non-Vegetarian'),
    ]
    name = models.CharField(max_length=100)
    pizza_type = models.CharField(max_length=20, choices=PIZZA_TYPE_CHOICES)
    image_url = models.URLField(max_length=1150)  # Store image URL instead of uploading
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# Order model to store pizza orders

class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, null=True)
    STATUS_CHOICES = [
        ('received', 'Order Received'),
        ('baking', 'Baking'),
        ('baked', 'Baked'),
        ('delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='received')

    def __str__(self):
        return f"Order for {self.full_name} ({self.pizza.name})"
        return f"{self.pizza.name} - {self.customer_name}"

    def update_status(self, new_status):
        self.status = new_status
        self.save()
