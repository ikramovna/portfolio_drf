from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.users.views import (RegisterAPIView, LogoutAPIView, VerifyAccountAPIView, ProjectDetailRetrieveAPIView,
                              ProjectSearchListAPIView, AllProjectModelViewSet, SendMailAPIView)

routers = DefaultRouter()
routers.register('project', AllProjectModelViewSet, basename='project-list-add')

urlpatterns = [
    path('', include(routers.urls)),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('logout', LogoutAPIView.as_view(), name='logout'),
    path('verify/<str:uid>/<str:token>', VerifyAccountAPIView.as_view(), name='verify'),
    path('project_detail/<int:pk>', ProjectDetailRetrieveAPIView.as_view()),
    path('project_search', ProjectSearchListAPIView.as_view()),
    path('send_mail', SendMailAPIView.as_view(), name='send_mail'),
]
