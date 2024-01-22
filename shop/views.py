from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm
from django.core.cache import cache


def main_page(request):
    return render(request, 'base.html')


def products_categories(request):
    products_categories = cache.get('all_categories')
    if not products_categories:
        products_categories = Category.objects.all()
        cache.set('all_categories', products_categories)
    return render(request, 'shop/products_categories.html', context={'categories': products_categories})


def list_products(request, category_slug):
    category_product = Category.objects.get(slug=category_slug)
    list_products = Product.objects.filter(
        category=category_product.id, available=True)
    return render(request, 'shop/list_products.html', context={'list_products': list_products,
                                                               'category_name': category_product})


def product_info(request, category_slug, product_slug):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_info.html', context={'product': product,
                                                              'cart_product_form': cart_product_form})
