from http import HTTPStatus

import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_api_create_user(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "name": "usuario",
        "email": "usuario@email.com",
        "username": "Usuario",
        "password": "SUp3rS3nh@",
    }
    response = client.post("/api/base/v1/users/", data=data)
    response_json = response.json()

    password = data.pop("password")
    assert response.status_code == HTTPStatus.CREATED

    assert response_json == data

    api = APIClient()
    response = api.post(
        "/api/auth/login/",
        data={
            "username": data["username"],
            "password": password,
        },
    )
    assert response.status_code == HTTPStatus.OK

    response_json = response.json()
    token = response_json.pop("token")
    assert token is not None
    assert response_json["user"] == data


@pytest.mark.django_db
def test_api_update_user(authenticated_test_user_client, create_test_user):
    user = create_test_user
    client = authenticated_test_user_client
    data = {
        "password": "SUp3rS3nh@",
    }
    response = client.patch(f"/api/base/v1/users/{user.pk}/", data=data)
    assert response.status_code == HTTPStatus.OK
    user.refresh_from_db()
    assert user.password != data["password"]
