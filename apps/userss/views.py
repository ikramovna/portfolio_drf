from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import (IsAuthenticated)
from rest_framework.response import (Response)
from rest_framework.views import (APIView)
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import (RefreshToken)

from userss.models import Project
from userss.serializers import AllProjectsModelSerializer, ProjectDetailModelSerializer, SendEmailSerializer, \
    UserSerializer, RegisterSerializer
from userss.services import (register_service, reset_password_service, reset_password_confirm_service)
from userss.tasks import send_email_customer



class AllProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = AllProjectsModelSerializer


class ProjectDetailRetrieveAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailModelSerializer


class ProjectSearchListAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailModelSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title_en', 'title_uz', 'title_ru', 'keyword_uz', 'keyword_en', 'keyword_ru']


class SendMailAPIView(GenericAPIView):
    serializer_class = SendEmailSerializer
    permission_classes = ()
    # @swagger_auto_schema(query_serializer=SendEmailSerializer, request_body=4)
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            message = serializer.validated_data.get('message')
            name = serializer.validated_data.get('name')
            phone = serializer.validated_data.get('phone')

            my_email = ''

            send_email_customer.delay(email, message, name, phone)
        except Exception as e:
            return Response({'success': False, 'message': str(e)})

        return Response({'success': True, 'message': 'Email sent!'})

