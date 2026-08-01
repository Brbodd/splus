from django.shortcuts import get_object_or_404, render
from .models import Product, ProductCategory

def product_list(request):

    products = Product.objects.all()

    category = request.GET.getlist("category")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    in_stock = request.GET.get("in_stock")

    if category:
        products = products.filter(category_id__in=category)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    if in_stock:
        products = products.filter(quantity__gt=0)

    sort = request.GET.get("sort")
    if sort == "cheap":
        products = products.order_by("price")

    elif sort == "expensive":
        products = products.order_by("-price")

    return render(
        request,
        "products/product_list.html",
        {
            "products": products
        }
    )


def product_detail(request, slug):

    product = get_object_or_404(Product, slug=slug)

    return render(
        request,
        "products/product_detail.html",
        {
            "product": product
        }
    )

def category_products(request, slug):
    pass

def brand_products(request, slug):
    pass