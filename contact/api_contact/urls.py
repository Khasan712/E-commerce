
from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_api_contact, name="create_api_contact"),
    path('get/<int:pk>/', views.get_api_contact, name="get_api_contact"),
    path('put/<int:pk>/', views.put_api_contact, name="put_api_contact"),
    path('delete/<int:pk>/', views.delete_api_contact, name="delete_api_contact"),
]
