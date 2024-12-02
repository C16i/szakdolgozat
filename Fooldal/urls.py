from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('shop/',views.shop)
]
