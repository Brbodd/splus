from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product-list'),
    path('category/<slug:slug>/', views.category_products, name='category-products'),
    path('brand/<slug:slug>/', views.brand_products, name='brand-products'),
    path('<slug:slug>/', views.product_detail, name='product-detail'),
]