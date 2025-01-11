from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_api_create_fazenda(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Fazenda X",
        "fardoes": 50,
        "rolinhos": 200,
    }
    response = client.post("/api/base/v1/fazendas/", data)
    assert response.status_code == HTTPStatus.CREATED

    response_json = response.json()
    pk = response_json.pop("id")
    assert pk is not None
    assert response_json == data


@pytest.mark.django_db
def test_api_create_fazenda_without_fields(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Fazenda X",
    }
    response = client.post("/api/base/v1/fazendas/", data)
    assert response.status_code == HTTPStatus.CREATED

    response_json = response.json()
    pk = response_json.pop("id")
    assert pk is not None
    assert response_json["nome"] == data["nome"]
    assert response_json["fardoes"] == 0
    assert response_json["rolinhos"] == 0


@pytest.mark.django_db
def test_api_create_fazenda_unique(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Fazenda X",
    }
    response = client.post("/api/base/v1/fazendas/", data)
    assert response.status_code == HTTPStatus.CREATED

    data = {
        "nome": "Fazenda X",
    }
    response = client.post("/api/base/v1/fazendas/", data)
    response_json = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response_json["nome"][0] == "Fazenda com este nome já existe."


@pytest.mark.django_db
def test_api_update_fazenda(authenticated_test_user_client, create_fazenda):
    client = authenticated_test_user_client
    fazenda = create_fazenda
    data = {
        "nome": "Fazenda Y",
    }
    response = client.put(f"/api/base/v1/fazendas/{fazenda.pk}/", data)
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    pk = response_json.pop("id")
    assert pk == str(fazenda.pk)
    assert response_json["nome"] == data["nome"]
    assert response_json["fardoes"] == fazenda.fardoes
    assert response_json["rolinhos"] == fazenda.rolinhos


@pytest.mark.django_db
def test_api_delete_fazenda(authenticated_test_user_client, create_fazenda):
    client = authenticated_test_user_client
    fazenda = create_fazenda
    response = client.delete(f"/api/base/v1/fazendas/{fazenda.pk}/")
    assert response.status_code == HTTPStatus.NO_CONTENT
