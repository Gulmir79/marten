from django.urls import path
from cart.views import CartView, AddToCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),


]