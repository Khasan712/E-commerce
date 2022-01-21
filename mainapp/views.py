from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
# Create your views here.
from .models import *
from custom_user.models import Custom_User


def index(request):
    mainCategory = MainCategory.objects.all()
    last_three = MainCategory.objects.all()[:3]
    product = Product.objects.all()

    
    context = {
        'mainCategory':mainCategory,
        'product':product,
        'last_three':last_three,
    }
    return render(request, 'index.html', context)



def products_list(request, pk):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    product = Product.objects.filter(main_category=pk)
    qty_product = product.count()
    category = ProductCategories.objects.filter(product_category=pk)
    

    context = {
        'product':product,
        'mainCategory':mainCategory,
        'category':category,
        'last_three':last_three,
        'qty_product':qty_product
    }
    return render(request, 'products/product_list.html', context)


def product_view(request, pk):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    product = Product.objects.get(id=pk)
    hit_count = HitCount.objects.get_for_object(product)
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    look_like_products = Product.objects.filter(product_category=pk)
    userProfile = Custom_User.objects.all()

    

    context = {
        'product':product,
        'hit_count_response':hit_count_response,
        'mainCategory':mainCategory,
        'last_three':last_three,
        'look_like_products':look_like_products,
        'userProfile':userProfile
    }
    return render(request, 'products/product.html', context)


def search(request):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            product = Product.objects.order_by('-date_published').filter(Q(title__icontains=q) | Q(description__icontains=q) | Q(main_category__category__icontains=q) | Q(product_category__title__icontains=q))
            qty_product = product.count()
    context = {
        'product':product,
        'mainCategory':mainCategory,
        'last_three':last_three,
        'qty_product':qty_product
    }
    return render(request, 'products/product_list.html', context)