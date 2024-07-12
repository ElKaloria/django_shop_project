from rest_framework import viewsets
from orders.models import Order, OrderItem
from orders.api.serializers import OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import BaseAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend, SearchFilter, OrderingFilter
    ]
    filterset_fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid']
    search_fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
    ordering_fields = ['id', 'first_name', 'last_name', 'created']


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [
        DjangoFilterBackend, OrderingFilter
    ]
    ordering_fields = ['id', 'price', 'quantity']
