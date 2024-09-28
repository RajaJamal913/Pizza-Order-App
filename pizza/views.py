from django.shortcuts import render, redirect, get_object_or_404
from .models import Pizza, Order
from .forms import OrderForm

# View to list pizzas and display ongoing orders
def pizza_list(request):
    pizzas = Pizza.objects.all()  # Ensure this returns pizza objects with valid IDs
    ongoing_orders = Order.objects.exclude(status='delivered')
    return render(request, 'pizza_list.html', {'pizzas': pizzas, 'ongoing_orders': ongoing_orders})


# Place order view
def place_order(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pizza = pizza
            order.save()
            return redirect('pizza_list')  # Redirect to pizza_list after placing the order
    else:
        form = OrderForm(initial={'pizza': pizza})
    
    return render(request, 'place_order.html', {'form': form, 'pizza': pizza})

# Order success page
def order_success(request):
    return render(request, 'order_success.html')

# View to check order status
def order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_status.html', {'order': order})


# views.py
from django.shortcuts import render

# Contact Us page view
def contact(request):
    return render(request, 'contact.html')
