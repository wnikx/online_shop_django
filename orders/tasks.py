from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"Номер заказа {order.id}"
    message = f"{order.first_name}!"\
        f"Вы успешно сделали заказ!"\
        f"Ваш номер заказа - {order.id}"
    mail_sent = send_mail(
        subject, message, 'admin@celskoemolochko.by', [order.email])
