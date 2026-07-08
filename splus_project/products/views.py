from django.shortcuts import render

def product_list(request):
    # products = Product.objects.all()

    # context = {
    #     "products": products,
    # }
    return render(request, "products/product_list.html")


def product_detail(request, slug):
    # product = get_object_or_404(Product, slug=slug)

    # context = {
    #     "product": product,
    # }
    return render(request, "products/product_detail.html")

def category_products(request, slug):
    pass

def brand_products(request, slug):
    pass