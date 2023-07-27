import json
import pytest

from django.conf import settings
from rest_framework.test import APIClient
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Project
from .serializers import AllProjectsModelSerializer


# class AllProductViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()
#         self.url = reverse('project-list-add-list')
#         self.project_data = {
#             'title_en': 'Test title2',
#             'title_ru': 'Test title2',
#             'title_uz': 'Test title2',
#             'description_en': 'Test description2',
#             'description_ru': 'Test description2',
#             'description_uz': 'Test description2',
#             'keyword': 'Test keyword2',
#             'url': 'https://github.com/Rahmet97/TestProject'
#         }
#
#     def test_create_project(self):
#         response = self.client.post(self.url, data=json.dumps(self.project_data), content_type='application/json')
#         self.assertEquals(response.status_code, 201)
#
#         self.assertEquals(Project.objects.count(), 1)
#         project = Project.objects.first()
#
#     def test_list_projects(self):
#         Project.objects.create(
#             title='Test title1',
#             description='Test description1',
#             keyword='Test keyword1',
#             url='https://github.com/Rahmet97/TestProjectBackend'
#         )
#         Project.objects.create(
#             title='Test title2',
#             description='Test description2',
#             keyword='Test keyword2',
#             url='https://github.com/Rahmet97/TestProjectBackend'
#         )
#         response = self.client.get(self.url)
#
#         self.assertEquals(response.status_code, 200)
#         first_project = response.json()[0]
#         self.assertIn('id', first_project)
#         self.assertEquals(first_project['title_en'], 'Test title1')
#         self.assertEquals(first_project['description_en'], 'Test description1')


def test_send_email():
    client = APIClient()
    url = reverse('send_mail')
    data = {
        'message': 'Test message',
        'name': 'Mirkomilov Oyatulloh',
        'phone': '+998999999999',
        'email': 'ruslanovrahmet@gmail.com'
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    url = reverse('register')
    data = {
        'first_name': 'Rahmatjon',
        'last_name': 'Ruslanov',
        'email': 'ruslanovrahmet@gmail.com',
        'username': 'Rahmet97',
        'password1': 'ab1234cd',
        'password2': 'ab1234cd'
    }

    response = client.post(url, data, format='json')
    assert response.status_code == 201