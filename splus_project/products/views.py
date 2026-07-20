from django.shortcuts import render
from .models import Product, Brand

def product_list(request):

    # products = Product.objects.all()

    products = [
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1051",
         "price": "۱۱.۲۹۰.۰۰۰",
         "quantity": 0,
         "slug": "seiko__ph_1051"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس زنانه",
         "code": "PH-1052",
         "price": "۱۲.۶۹۰.۰۰۰",
         "quantity": 3,
         "slug": "seiko__ph_1052"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "کاسیو پلاس مردانه",
         "code": "PH-1053",
         "price": "۱۰.۱۹۰.۰۰۰",
         "quantity": 10,
         "slug": "casio__ph_1053"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1054",
         "price": "۱۵.۰۰۰.۰۰۰",
         "quantity": 1,
         "slug": "seiko__ph_1054"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه و زنانه",
         "code": "PH-1055",
         "price": "۹.۸۰۷.۰۰۰",
         "quantity": 0,
         "slug": "seiko__ph_1055"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس زنانه",
         "code": "PH-1056",
         "price": "۱۰.۸۰۷.۰۰۰",
         "quantity": 3,
         "slug": "seiko__ph_1056"},        
         {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو مردانه",
         "code": "PH-1058",
         "price": "۱۱.۰۰۰.۰۰۰",
         "quantity": 7,
         "slug": "seiko__ph_1058"},        
         {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه و زنانه",
         "code": "PH-1059",
         "price": "۱۲.۲۳۰.۰۰۰",
         "quantity": 5,
         "slug": "seiko__ph_1059"},         
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

    '''
    just write this lines after run DB
    from django.shortcuts import get_object_or_404

    product = get_object_or_404(Product, slug=slug)
    '''

    products = [
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1051",
         "price": "۱۱.۲۹۰.۰۰۰",
         "quantity": 0,
         "slug": "seiko__ph_1051"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس زنانه",
         "code": "PH-1052",
         "price": "۱۲.۶۹۰.۰۰۰",
         "quantity": 3,
         "slug": "seiko__ph_1052"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "کاسیو پلاس مردانه",
         "code": "PH-1053",
         "price": "۱۰.۱۹۰.۰۰۰",
         "quantity": 10,
         "slug": "casio__ph_1053"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه",
         "code": "PH-1054",
         "price": "۱۵.۰۰۰.۰۰۰",
         "quantity": 1,
         "slug": "seiko__ph_1054"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه و زنانه",
         "code": "PH-1055",
         "price": "۹.۸۰۷.۰۰۰",
         "quantity": 0,
         "slug": "seiko__ph_1055"},
        {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس زنانه",
         "code": "PH-1056",
         "price": "۱۰.۸۰۷.۰۰۰",
         "quantity": 3,
         "slug": "seiko__ph_1056"},        
         {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو مردانه",
         "code": "PH-1058",
         "price": "۱۱.۰۰۰.۰۰۰",
         "quantity": 7,
         "slug": "seiko__ph_1058"},        
         {"img": "https://www.seikopluswatch.com/wp-content/uploads/2024/08/seikoplus.png",
         "name": "سیکو پلاس مردانه و زنانه",
         "code": "PH-1059",
         "price": "۱۲.۲۳۰.۰۰۰",
         "quantity": 5,
         "slug": "seiko__ph_1059"},         
    ]

    product = None

    for item in products:
        if item["slug"] == slug:
            product = item
            break

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