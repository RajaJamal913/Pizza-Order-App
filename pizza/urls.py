from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza_list, name='pizza_list'),
    path('order/<int:pizza_id>/', views.place_order, name='place_order'),
    path('order/success/', views.order_success, name='order_success'),
    path('order/status/<int:order_id>/', views.order_status, name='order_status'),
    path('contact/', views.contact, name='contact'),  # Add this path to avoid ReverseMatch error
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
