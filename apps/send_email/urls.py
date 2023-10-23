from django.urls import path

from apps.send_email.views import SendMailAPIView

urlpatterns = [
    path('send_mail_user', SendMailAPIView.as_view(), name='send_mail'),
]
