from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.main_page),
    path('products_categories/', views.products_categories,
         name='products_categories'),
]
