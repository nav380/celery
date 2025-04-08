from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .tasks import send_notification_email

@receiver(post_save, sender=User)
def user_created_handler(sender, instance, created, **kwargs):
    print(f"User created: {instance.username}")
    if created:
        send_notification_email.delay(instance.id, "Welcome to the platform!")
