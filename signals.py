from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ComingSoonNotice


@receiver(post_save, sender=ComingSoonNotice)
def send_mail_on_create(sender, instance, created, *args, **kwargs):
	if created:
		instance.send_verification_email()
