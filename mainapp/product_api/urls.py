
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('<int:pk>/view/', views.api_product_view, name='detail'),
    path('<int:pk>/update/', views.api_product_update, name='update'),
    path('<int:pk>/delete/', views.api_product_delete, name='delete'),
    path('create/', views.api_product_create, name='create'),
]



