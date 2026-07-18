from django.shortcuts import render
from .models import Product, Brand

def product_list(request):

    # products = Product.objects.all()

    products = [
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1051",
         "price": "۱۱.۲۹۰.۰۰۰"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1052",
         "price": "۱۲.۶۹۰.۰۰۰"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1053",
         "price": "۱۰.۱۹۰.۰۰۰"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1054",
         "price": "۱۵.۰۰۰.۰۰۰"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس زنانه",
         "code": "PH-1055",
         "price": "۱۷.۴۹۰.۰۰۰"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": " ست سیکو پلاس مردانه",
         "code": "PH-1056",
         "price": "۱۳.۸۹۰.۰۰۰"},
    ]

    # type = request.GET.getlist("type")
    # min_price = request.GET.get("min_price")
    # max_price = request.GET.get("max_price")
    # in_stock = request.GET.get("in_stock")

    # if brand:
    #     products = products.filter(brand__slug__in=brand)

    # if min_price:
    #     products = products.filter(price__gte=min_price)

    # if max_price:
    #     products = products.filter(price__lte=max_price)

    # if in_stock:
    #     products = products.filter(quantity__gt=0)

    # sort = request.GET.get("sort")
    # if sort == "cheap":
    #     products = products.order_by("price")

    # elif sort == "expensive":
    #     products = products.order_by("-price")

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
    return render(request, "products/product_detail.html")

def category_products(request, slug):
    pass

def brand_products(request, slug):
    pass