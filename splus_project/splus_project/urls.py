from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    path('orders/', include('orders.urls')),
    path('products/', include('products.urls')),
    path('contact-us/', include('contact_module.urls')),
    path('shopping-cart/', include('shopping_module.urls'))
]
