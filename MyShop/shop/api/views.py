from rest_framework import viewsets
from .serializers import *
from shop.models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BaseAuthentication


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
