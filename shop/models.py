from django.db import models
from django.urls import reverse


class Category(models.Model):
    category_name = models.CharField(
        max_length=200, verbose_name='Имя категории')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


def get_absolute_url(self):
    return reverse('shop/list_categories.html', args=(self.slug,))


class Product(models.Model):
    LITER = "л"
    KILOGGRAM = "кг"
    MEASURMENT_UNIT_CHOICES = [
        (LITER, 'литр'),
        (KILOGGRAM, 'килограмм'),
    ]

    product_name = models.CharField(max_length=200, verbose_name='Имя товара')
    slug = models.SlugField(max_length=200)
    category = models.ForeignKey(
        Category, related_name='category', on_delete=models.CASCADE, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, verbose_name='Цена')
    image = models.ImageField(upload_to='products',
                              verbose_name='Изображение', blank=True)
    min_volume = models.DecimalField(max_digits=3,
                                     decimal_places=2, verbose_name='Мин. кол-во')
    aging = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name='Выдержка', default=0)
    unit = models.CharField(max_length=2,
                            choices=MEASURMENT_UNIT_CHOICES, default=KILOGGRAM, verbose_name='Ед. измерения')
    available = models.BooleanField(default=True, verbose_name='Доступность')

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['category']

    def __str__(self):
        return self.product_name


def get_absolute_url(self):
    return reverse('shop/product_info.html', args=(self.slug, self.category))
