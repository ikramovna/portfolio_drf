from rest_framework.serializers import ModelSerializer, Serializer, CharField, EmailField

from apps.portfolio.models import Project


class AllProjectsModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = (
            'id', 'title', 'description', 'image')


class ProjectDetailModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'



