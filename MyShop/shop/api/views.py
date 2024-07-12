from rest_framework import viewsets
from .serializers import *
from shop.models import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BaseAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend, SearchFilter, OrderingFilter
    ]
    filterset_fields = ['name', 'description', 'price', 'available']
    search_fields = ['name', 'description']
    ordering_fields = ['id', 'name', 'price', 'created']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend, SearchFilter, OrderingFilter
    ]
    filterset_fields = ['id', 'name']
    search_fields = ['name']
    ordering_fields = ['id', 'name']
