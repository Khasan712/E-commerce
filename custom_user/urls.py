from django.urls import path
from . import views

urlpatterns = [
    path('user-register', views.user_register, name='user_register'),
    path('user-login', views.user_login, name='user_login'),
    path('logout/user', views.user_logout, name='user_logout'),
    path('user/<str:username>/profile', views.user_profile, name='user_profile'),
    path('edit/<str:username>/profile', views.edit_profile, name='edit_profile'),
    # path('post/<int:pk>/edit', views.update_user_post, name='update_user_post'),
    # path('post/<int:pk>/delete', views.delete_user_post, name='delete_user_post'),
]