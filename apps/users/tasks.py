import os

from celery import shared_task
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


# Send email
@shared_task
def send_email_customer(email, message, name, phone):
    print('Sending message')
    msg = f'''
    {email}, {message}, {name}, {phone}
    '''
    print(msg)
    send_mail(
        subject="Hello",
        message=msg,
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=[email],
        fail_silently=False,
    )
