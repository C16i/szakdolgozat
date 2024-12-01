from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('shop/',views.shop),
    path('termekek/', views.termek_list, name='termek-list'),
    path('termekek/hozzaadas/', views.termek_create, name='termek-create'),
    path('termekek/modositas/<int:pk>/', views.termek_update, name='termek-update'),
    path('termekek/torles/<int:pk>/', views.termek_delete, name='termek-delete'),
]
