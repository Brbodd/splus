from django.shortcuts import render
from django.views.generic.base import View


class ShoppingCartView(View):


    def get(self, request):
        return render(
            request,
            'shopping_module/shopping_cart.html')

    def post(self, request):
        return render(
            request,
            'shopping_module/shopping_cart.html')

