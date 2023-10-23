from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView

from apps.portfolio.models import Project
from apps.portfolio.serializers import AllProjectsModelSerializer, ProjectDetailModelSerializer


class AllProjectListCreateAPIView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = AllProjectsModelSerializer


class ProjectDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailModelSerializer


class ProjectSearchListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'keyword']
