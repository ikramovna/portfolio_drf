from django.urls import path

from apps.portfolio.views import ProjectSearchListAPIView, ProjectDetailRetrieveAPIView, AllProjectListCreateAPIView

urlpatterns = [
    path('project', AllProjectListCreateAPIView.as_view()),
    path('project_detail/<int:pk>', ProjectDetailRetrieveAPIView.as_view()),
    path('project_search', ProjectSearchListAPIView.as_view()),
]
