import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from src.base.models import Algodoeira, Fazenda

User = get_user_model()


@pytest.fixture
def create_test_user():
    user, _ = User.objects.get_or_create(
        username="test",
        email="test@test.com",
        defaults=dict(
            password="test123",
        ),
    )

    return user


@pytest.fixture
def create_algodoeira():
    algodoeira, _ = Algodoeira.objects.get_or_create(
        nome="<NAME>",
        producao=10,
    )

    return algodoeira


@pytest.fixture
def create_fazenda():

    fazenda, _ = Fazenda.objects.get_or_create(
        nome="<NAME>",
        fardoes=10,
        rolinhos=10,
    )

    return fazenda


@pytest.fixture
def client_api():
    return APIClient()


@pytest.fixture
def authenticated_test_user_client(client_api, create_test_user):
    client_api.force_authenticate(user=create_test_user)
    return client_api


@pytest.fixture
def create_user_and_authenticate_client(client_api, create_test_user):
    def make_client(**kwargs):
        user = create_user(**kwargs)
        client_api.force_authenticate(user=user)
        return client_api

    return make_client


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)

    return make_user
