from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from hitcount.models import HitCount
from hitcount.views import HitCountMixin
from pip import main
# Create your views here.
from .models import *
from .filters import ProductItemsFilter
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



def products_list(request, main_slug):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    mainCategory_p = MainCategory.objects.all().filter(main_slug=main_slug).first()
    product = Product.objects.filter(main_category__main_slug=main_slug, top_or_new="")

    q_color = []
    for pro in product:
        for ctg in pro.color.all():
            q_color.append(ctg)
    qty_color = len(q_color)

    q_size = []
    for pro in product:
        for ctg in pro.size.all():
            q_size.append(ctg)
    qty_size = len(q_size)

    q_category = []
    for pro in product:
        for ctg in pro.product_category.all():
            print(ctg)
            q_category.append(ctg)
            # print(q_category)
    qty_category = len(q_category)


    qty_product = product.count()
    f = ProductItemsFilter(request.GET, queryset=Product.objects.all())

    category = request.GET.get('q')
    if category == None:
        product = Product.objects.filter(main_category__main_slug=main_slug, top_or_new="")
        # if product:
        #     categories = ProductCategories.objects.all().filter(product_category=id).distinct()
    else:
        product = Product.objects.filter(
            main_category__main_slug=main_slug,
            product_category__title=category,
            top_or_new=""
        ).order_by('-hit_count_generic__hits')
    categories = ProductCategories.objects.filter(product_category__title=id).distinct()

    context = {
        'product':product,
        'mainCategory':mainCategory,
        'category':category,
        'last_three':last_three,
        'qty_product':qty_product,
        'filter':f,
        'mainCategory_p':mainCategory_p,
        'categories':categories,
        'qty_color':qty_color,
        'qty_size':qty_size,
        'qty_category':qty_category,
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
            product = Product.objects.order_by('-date_published').filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(main_category__category__icontains=q) |
                Q(product_category__title__icontains=q)
            ).distinct()

            qty_product = product.count()
    context = {
        'product':product,
        'mainCategory':mainCategory,
        'last_three':last_three,
        'qty_product':qty_product
    }
    return render(request, 'products/product_list.html', context)