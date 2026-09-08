from django.db import models
from django.urls import reverse


class ProductCategory(models.Model):
    title = models.CharField(
        default='',
        max_length=100,
        verbose_name='عنوان'
    )

    url_title = models.SlugField(
        default='',
        verbose_name='عنوان در url'
    )

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='نام محصول'
    )

    slug = models.SlugField(
        default='',
        null=False,
        unique=True
    )

    code = models.CharField(
        max_length=50,
        verbose_name='کد محصول'
    )

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name='دسته بندی'
    )

    price = models.PositiveIntegerField(
        verbose_name='قیمت'
    )

    quantity = models.PositiveIntegerField(
        default=0,
        verbose_name='موجودی'
    )

    image_src = models.CharField(
        max_length=350,
        verbose_name='آدرس عکس'
    )

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} ({self.code})'