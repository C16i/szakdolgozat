from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.homepage),
    path('shop/',views.shop),
    path('termekek/', views.termek_list, name='termek-list'),
    path('termekek/hozzaadas/', views.termek_create, name='termek-create'),
    path('termekek/modositas/<int:pk>/', views.termek_update, name='termek-update'),
    path('termek/delete/<int:pk>/', views.termek_delete, name='termek-delete'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
]
