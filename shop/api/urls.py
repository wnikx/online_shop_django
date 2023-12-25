from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.ProductCreateView.as_view(), name='product_list'),
    path('products/drf-auth', include('rest_framework.urls')),
    path('products/<int:pk>/', views.ProductCreateView.as_view(),
         name='product_detail'),
]
#
