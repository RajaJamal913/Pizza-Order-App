from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'address', 'phone_number', 'pizza']
        widgets = {
            'pizza': forms.HiddenInput()
        }
