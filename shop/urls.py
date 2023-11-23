from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('products/', views.products_categories,
         name='products'),
    path('products/<slug:category_slug>',
         views.list_products, name='list_products'),

]
