import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_one_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)
    # Act
    response = client.get(f"/api/v1/courses/{course[0].id}/")
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course[0].id


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get('/api/v1/courses/')
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, course in enumerate(data):
        assert course['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=10)
    # Act
    response = client.get('/api/v1/courses/', {'id': courses[0].id})
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[0].id


@pytest.mark.django_db
def test_filter_name_courses(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=4)
    # Act
    response = client.get('/api/v1/courses/', {'name': courses[1].name})
    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[1].name


@pytest.mark.django_db
def test_post_course(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', {'name': 'Django'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    courses = course_factory(_quantity=15)
    response = client.patch(f'/api/v1/courses/{courses[2].id}/', {'name': 'Python'})

    assert response.status_code == 200
    data = response.json()
    assert Course.objects.get(id=courses[2].id).name == 'Python'


@pytest.mark.django_db
def test_del_course(client, course_factory):
    courses = course_factory(_quantity=15)
    count = Course.objects.count()
    response = client.delete(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1
