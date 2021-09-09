from django.shortcuts import render, redirect
from shoptest_app.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def personalCart(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def addCart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=personalCart(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = personalCart(request)
        )
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cartDetails(request, total=0, counter=0, cart_item = None):
    try:
        cart = Cart.objects.get(cart_id=personalCart(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quanitity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items = cart_items, total = total, counter = counter))