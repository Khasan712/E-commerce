from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/<int:pk>', views.blog_view, name='blog_view'),
]