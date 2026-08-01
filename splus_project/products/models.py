from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='', null=False, unique=True)
    code = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, default='', on_delete=models.CASCADE, related_name='products')
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default='', null=False)
    image_src = models.CharField(default='', max_length=350)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("product-detail", args=[self.slug])
    
    def __str__(self):
        return f"{self.name} ({self.code})"