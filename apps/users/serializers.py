from django.contrib.auth.models import User
from rest_framework.fields import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import Project


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class AllProjectsModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = 'id', 'title', 'description', 'image', 'image1'


class ProjectDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class SendEmailSerializer(Serializer):
    message = CharField(max_length=500)
    name = CharField(max_length=100)
    phone = CharField(max_length=55)
    email = EmailField()


