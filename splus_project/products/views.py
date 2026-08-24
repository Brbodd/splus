from django.views.generic import ListView, DetailView
from .models import Product

class ProductListView(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_objects_name = 'products'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)



class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
