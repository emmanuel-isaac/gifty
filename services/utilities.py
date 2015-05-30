from django.core.mail import EmailMultiAlternatives

# Utility functions

def send_django_mail(subject, from_email, to, html_content=None):
    msg = EmailMultiAlternatives(subject, "text body", from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()

