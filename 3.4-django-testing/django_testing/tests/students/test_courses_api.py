from venv import create
import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from students.models import Student, Course

def test_app():
    assert 2 == 2

@pytest.mark.django_db
def test_api():
    client = APIClient()
    User.objects.create_user('odmin')
    Course.objects.create(name='Ajax')

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json
    # assert len(data) == 1
    assert data[0] == 'Ajax'
