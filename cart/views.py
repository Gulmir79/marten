from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from product.models import Product
from cart.models import Cart, CartItem


# Create your views here.


class CartView(LoginRequiredMixin, View):
    template_name = 'cart.html'

    def get(self, request):
        cart, carted = Cart.objects.get_or_create(user=request.user)
        return render(request, self.template_name, {'cart:cart'})

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product=get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)


        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()
            messages.info(request, message='Количество товара увеличено')
        else:
            messages.success(request, message='Товар добавлен в карзину')
        return redirect('cart')