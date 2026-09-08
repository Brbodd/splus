from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):

    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'


class ProductDetailView(DetailView):

    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'