from django.shortcuts import redirect, render
from django.http import HttpResponse
import datetime
from django.contrib import messages
from orders.models import Order
# Create your views here.
from project_cart.models import CartItem
from .forms import OrderForm



def payments(request):
    return render(request, 'order/payments.html')


def order(request, total=0, quantity=0):
    user = request.user

    cart_items = CartItem.objects.filter(user=user)
    qty_cart_item = cart_items.count()



    if qty_cart_item <= 0:
        messages.warning(request, 'Your account expires in three days.')
        return redirect('checkout')

    tax = 0
    total_amount = 0
    for cart_item in cart_items:
        total += (cart_item.product.price * cart_item.product.qty_product)
        quantity += cart_item.product.qty_product
    tax = (1 * total)/100
    total_amount = total + tax


    form = OrderForm(request.POST)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.user = user
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phone']
            data.country = form.cleaned_data['country']
            data.city = form.cleaned_data['city']
            data.state = form.cleaned_data['state']
            data.address_line_1 = form.cleaned_data['address_line_1']
            data.address_line_2 = form.cleaned_data['address_line_2']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = total_amount
            data.tax = tax
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()


            # Generate order number
            yr = int(datetime.date.today().strftime('%Y'))
            dt = int(datetime.date.today().strftime('%d'))
            mt = int(datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            order = Order.objects.get(user=user, is_ordered=False, order_number=order_number)

            context = {
                'cart_items':cart_items,
                'order':order,
                'total':total,
                'tax':tax,
                'total_amount':total_amount
            }
            return render(request, 'order/payments.html', context)
    else:
        return redirect('checkout')


    