from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import requests
import json

# custom_user Forms
from .forms import CreatePostForm, Custom_UsereForm, EditCustom_UserForm
from .models import Custom_User
from mainapp.models import *
from project_cart.models import Cart, CartItem
from project_cart.views import _cart_id
from mainapp.models import Product


# User register
def user_register(request):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = Custom_UsereForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was creatd for ' + user)
                user = form.save()

                return redirect('user_login')
            else:
                messages.error(request, "Error")
        else:
            form = Custom_UsereForm()
    
    context = {
        'form':form,
        'mainCategory':mainCategory,
        'last_three':last_three,
    }
    return render(request, 'custom_user/register.html', context)


# User Login
def user_login(request):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                try:
                    cart = Cart.objects.get(cart_id=_cart_id(request))
                    if_cart_is_exist = CartItem.objects.filter(cart=cart).exists()
                    if if_cart_is_exist:
                        cart_item = CartItem.objects.filter(cart=cart)
                        for c_item in cart_item:
                            c_item.user = user
                            c_item.save()
                except:
                    pass
                login(request, user)
                return redirect('index')
            elif user is None:
                messages.warning(request, 'Not found that acoount')
            else:
                messages.error(request, 'Username or password did not match')
    
    context = {
        'last_three':last_three,
        'mainCategory':mainCategory,
    }
    return render(request, 'custom_user/login.html', context)


# User loag out
def user_logout(request):
    logout(request)
    return redirect('index')

def user_profile(request, username):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    userProfile = Custom_User.objects.get(username=username)

    user = request.user
    product_user = Custom_User.objects.filter(username=username).first()
    post_products = Product.objects.filter(product_user=product_user)

    form = CreatePostForm()
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            product_user = Custom_User.objects.filter(username=user.username).first()
            obj.product_user = product_user
            obj.save()
            form.save_m2m()
            return redirect('user_profile', user.username)

    res = requests.get('http://ip-api.com/json/')
    res_data = res.text
    geo_data = json.loads(res_data)
    # print(geo_data)
    

    context = {
        'userProfile':userProfile,
        'last_three':last_three,
        'mainCategory':mainCategory,
        'geo_data':geo_data,
        'form':form,
        'user':user,
        'post_products':post_products,
    }
    return render(request, 'custom_user/profile.html', context)


def edit_profile(request, username):
    last_three = MainCategory.objects.all()[:3]
    mainCategory = MainCategory.objects.all()
    userProfile = Custom_User.objects.get(username=username)
    form = EditCustom_UserForm(request.POST or None, request.FILES or None, instance=userProfile)
    if request.method == 'POST':
        form = EditCustom_UserForm(request.POST, request.FILES, instance=userProfile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', userProfile.id)


    context = {
        'userProfile':userProfile,
        'form':form,
        'last_three':last_three,
        'mainCategory':mainCategory,
    }
    return render(request, 'custom_user/edit_profile.html', context)