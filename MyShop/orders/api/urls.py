from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'orders'

router = DefaultRouter()
router.register(r'order', views.OrderViewSet, basename='order')
router.register(r'order_item', views.OrderItemViewSet, basename='order_item')


urlpatterns = [
    path('', include(router.urls)),
]