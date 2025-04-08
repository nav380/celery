from celery import shared_task
from django.core.mail import send_mail
from .models import Notification
from django.contrib.auth.models import User

@shared_task
def send_notification_email(user_id, message):
    try:
        user = User.objects.get(id=user_id)
        Notification.objects.create(user=user, message=message)
        send_mail(
            subject='New Notification',
            message=message,
            from_email='naveenchauhan380@gmail.com',
            recipient_list=["navcha052@gmail.com"],
            fail_silently=False,
        )
    except User.DoesNotExist:
        pass