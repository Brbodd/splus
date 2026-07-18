from django.shortcuts import render
from .models import Product, Brand

def product_list(request):

    products = Product.objects.all()
    # products = range(9)

    brand = request.GET.getlist("brand")
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")
    in_stock = request.GET.get("in_stock")

    if brand:
        products = products.filter(brand__slug__in=brand)

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

    # elif sort == "newest":
    #     products = products.order_by("-created_at")

    return render(
        request,
        "products/product_list.html",
        {
            "products": products
        }
    )


def product_detail(request, slug):
    # products = [
    #     {
    #         "name": "Casio A158",
    #         "code": "PH-1051"
    #     },
    #     {
    #         "name": "Seiko 5",
    #         "code": "PH-1052"
    #     },
    #     {
    #         "name": "Citizen Eco Drive",
    #         "code": "PH-1053"
    #     }
    # ]
    products = range(9)
    return render(request, "products/product_detail.html", { 'products': products })

def category_products(request, slug):
    pass

def brand_products(request, slug):
    pass