from rest_framework.generics import GenericAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from apps.send_email.serializers import SendEmailSerializer
from apps.send_email.tasks import send_email_customer


class SendMailAPIView(GenericAPIView):
    serializer_class = SendEmailSerializer
    permission_classes = ()
    parser_classes = (FormParser, MultiPartParser)

    # @swagger_auto_schema(query_serializer=SendEmailSerializer, request_body=4)
    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            email = serializer.validated_data.get('email')
            message = serializer.validated_data.get('message')
            name = serializer.validated_data.get('name')
            phone = serializer.validated_data.get('phone')

            send_email_customer.delay(email, message, name, phone)
        except Exception as e:
            return Response({'success': False, 'message': str(e)})

        return Response({'success': True, 'message': 'Email sent!'})
