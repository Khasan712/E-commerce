from django.shortcuts import get_object_or_404, render, redirect
from mainapp.models import *
from project_cart.models import CartItem, Cart
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from cupons.forms import CuponApllyForm

from mainapp.models import *

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def cart_add(request, product_id):
    product = Product.objects.get(id=product_id) # get product ID
    try:
        
        cart = Cart.objects.get(cart_id=_cart_id(request)) # get cart ID from session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id=_cart_id(request)
        )
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.product.qty_product += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart
        )
        cart_item.save()
    # return HttpResponse(cart_item.product.price)
    # exit()
    return redirect('cart')







def cart(request, total=0, quantity=0, cart_items=None):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    try:
        tax = 0
        total_amount = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.product.qty_product)
                quantity += cart_item.product.qty_product
            tax = (1 * total)/100
            total_amount = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'total_amount':total_amount,
        'mainCategory':mainCategory,
        'last_three':last_three,
    }
    return render(request, 'products/cart.html', context)


def delete_cart_item(request, product_id):
    if request.user.is_authenticated:
        cart_item = CartItem.objects.filter(user=request.user)
        cart_item.delete()
        return redirect('cart')
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        product = get_object_or_404(Product, id=product_id)
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.delete()
        return redirect('cart')

@login_required(login_url='user_login')
def checkout(request, total=0, quantity=0, cart_items=None):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()

    try:
        tax = 0
        total_amount = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            for cart_item in cart_items:
                total += (cart_item.product.price * cart_item.product.qty_product)
                quantity += cart_item.product.qty_product
            tax = (1 * total)/100
            total_amount = total + tax
    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'total_amount':total_amount,
        'mainCategory':mainCategory,
        'last_three':last_three,
    }
    return render(request, 'products/checkout.html', context)
