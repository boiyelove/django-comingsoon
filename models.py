import uuid
from django.db import models
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse_lazy
from django.conf import settings

# Create your models here.
class ComingSoonNotice(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	email = models.EmailField(unique = True)
	verification_link = models.UUIDField(default=uuid.uuid4, editable=False)
	verified = models.BooleanField(default=False)
	referral = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, editable=False)


	def send_verification_email(self):
		email_subject = "Yay! you're almost done"
		ver_url = reverse_lazy("comingsoon:verify-signup", kwargs={"slug":self.verification_link})

		email_body_text = f"Kindly verify your email so we can nofify you when Streetmarket is live.\nClick the link below to verify your email: {settings.SITE_URL}{ver_url} \n Alternatively, you can copy the link into your browser to complete the signup process."
		email_html_content = f"Kindly verify your email so we can nofify you when Streetmarket is live.\n<a href='{settings.SITE_URL}{ver_url}'>Click here to verify your email</a>\nAlternatively, you can copy the link into your browser to complete the signup process.{settings.SITE_URL}{ver_url}."
		email_from = settings.DEFAULT_FROM_EMAIL
		email_to = [self.email]
		# email_reply_to = []
		# headers ={}
		email = EmailMultiAlternatives(
			email_subject,
			email_body_text ,
			email_from,
			email_to,
			# email_reply_to,
			# email_headers
			)
		email.attach_alternative(email_html_content, "text/html")
		email.send()

	def send_verification_complete_mail(self):
		email_subject = "Congratulation! You've done it"
		email_body_text = "We will now notify you when Streetmarket becomes live. \n In the mean time, tell your friends about Streetmarket!"
		email_html_text = "We will now notify you when Streetmarket becomes live. \n In the mean time, tell your friends about Streetmarket!"
		email_from = settings.DEFAULT_FROM_EMAIL
		email_to = [self.email]
		# email_reply_to = []
		# headers ={}
		email = EmailMultiAlternatives(
			email_subject,
			email_body,
			email_from,
			email_to,
			# email_reply_to,
			# email_headers
			)
		email.attach_alternative(html_content, "text/html")
		email.send()


