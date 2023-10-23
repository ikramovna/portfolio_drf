from rest_framework.serializers import Serializer, CharField, EmailField


class SendEmailSerializer(Serializer):
    message = CharField(max_length=500)
    name = CharField(max_length=100)
    phone = CharField(max_length=55)
    email = EmailField()
