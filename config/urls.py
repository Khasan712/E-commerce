"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_api.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('custom/user/', include('custom_user.urls')),
    path('', include('mainapp.urls')),
     path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('blog/', include('blog.urls')),
    path('cart/', include('project_cart.urls')),
    path('orders/', include('orders.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('cart/', include(('project_cart.urls','cart') ,namespace='cart')),
    # path('comments/', include('comments_user.urls')),

    # Rest Api
    path('api/product/', include('mainapp.product_api.urls', 'product_api')),
    path('api/user/', include('custom_user.api_custom.urls')),
    path('api/contact/user/', include('contact.api_contact.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

