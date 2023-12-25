from rest_framework import generics
from .serializers import ProductSerializer
from shop.models import Product
from .permissions import IsAdminOrReadOnly


class ProductCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)
