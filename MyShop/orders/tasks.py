from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from MyShop.settings import EMAIL_HOST_USER


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер {order.id}'
    message = f'Здравствуйте, {order.first_name},\n\n' \
              f'Вы оформили заказ номер {order.id}.\n' \
              f'Ваш заказ будет доставлен по адресу {order.address}.\n'
    mail_send = send_mail(subject, message, EMAIL_HOST_USER, [order.email])
    return mail_send
