from http import HTTPStatus

import pytest

from src.base.models import Algodoeira


@pytest.mark.django_db
def test_api_create_algodoeira(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Algodoeira X",
        "producao": 1000,
    }
    response = client.post("/api/base/v1/algodoeiras/", data)
    assert response.status_code == HTTPStatus.CREATED

    response_json = response.json()
    pk = response_json.pop("id")
    assert pk is not None
    assert response_json == data


@pytest.mark.django_db
def test_api_create_algodoeira_without_fields(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Algodoeira X",
    }
    response = client.post("/api/base/v1/algodoeiras/", data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_json = response.json()

    assert response_json["producao"][0] == "Este campo é obrigatório."


@pytest.mark.django_db
def test_api_create_algodoeira_producao_zero(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Algodoeira X",
        "producao": 0,
    }
    response = client.post("/api/base/v1/algodoeiras/", data)
    assert response.status_code == HTTPStatus.BAD_REQUEST

    response_json = response.json()

    assert (
        response_json["producao"][0]
        == "Certifque-se de que este valor seja maior ou igual a 1."
    )


@pytest.mark.django_db
def test_api_create_algodoeira_unique(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "nome": "Algodoeira X",
        "producao": 1000,
    }
    response = client.post("/api/base/v1/algodoeiras/", data)
    assert response.status_code == HTTPStatus.CREATED

    data = {
        "nome": "Algodoeira X",
        "producao": 1000,
    }
    response = client.post("/api/base/v1/algodoeiras/", data)
    response_json = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response_json["nome"][0] == "Algodoeira com este nome já existe."


@pytest.mark.django_db
def test_api_update_algodoeira(authenticated_test_user_client, create_algodoeira):
    client = authenticated_test_user_client
    algodoeira = create_algodoeira
    data = {
        "nome": "Algodoeira Y",
    }
    response = client.patch(f"/api/base/v1/algodoeiras/{algodoeira.pk}/", data)
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    pk = response_json.pop("id")
    assert pk == str(algodoeira.pk)
    assert response_json["nome"] == data["nome"]
    assert response_json["producao"] == algodoeira.producao


@pytest.mark.django_db
def test_api_delete_algodoeira(authenticated_test_user_client, create_algodoeira):
    client = authenticated_test_user_client
    algodoeira = create_algodoeira
    response = client.delete(f"/api/base/v1/algodoeiras/{algodoeira.pk}/")
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_api_pagination_algodoeira(authenticated_test_user_client):
    for row in range(1, 50):
        Algodoeira.objects.create(
            nome=f"Algodoeira {row}",
            producao=row * 100,
        )

    client = authenticated_test_user_client
    response = client.get("/api/base/v1/algodoeiras/?skip=20&take=20")
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()

    assert "total" in response_json
    assert "data" in response_json
    assert "links" in response_json
    assert response_json["links"]["next"] is not None
    assert response_json["links"]["previous"] is not None
    assert response_json["total"] == 49


@pytest.mark.django_db
def test_api_search_algodoeira(authenticated_test_user_client):
    for row in range(1, 50):
        Algodoeira.objects.create(
            nome=f"Algodoeira {row}",
            producao=row * 100,
        )

    client = authenticated_test_user_client
    response = client.get("/api/base/v1/algodoeiras/?search=1")
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()

    assert "total" in response_json
    assert response_json["total"] == 14
