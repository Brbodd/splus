from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShoppingCartView.as_view(), name='shopping-cart'),
    # path('add/', views.ShoppingCartView.as_view(), name='shopping-cart'),
    # path('delete/', views.ShoppingCartView.as_view(), name='shopping-cart'),
]