from datetime import datetime, timedelta
from http import HTTPStatus

import pytest


@pytest.mark.django_db
def test_api_create_cenario(authenticated_test_user_client):
    client = authenticated_test_user_client
    data = {
        "inicio": "2025-01-11",
        "nome": "<NAME>",
    }
    response = client.post("/api/simulador/v1/cenarios/", data=data)
    assert response.status_code == HTTPStatus.CREATED
    response_json = response.json()
    pk = response_json.pop("id")
    assert pk is not None
    assert response_json["inicio"] == data["inicio"]
    assert response_json["nome"] == data["nome"]
    assert response_json["dias"] == 0
    assert response_json["termino"] == data["inicio"]
    assert response_json["fardoes"] == 0
    assert response_json["rolinhos"] == 0
    assert response_json["total_fardos"] == 0


@pytest.mark.django_db
def test_api_update_cenario(
    authenticated_test_user_client, create_cenario, create_fazenda, create_algodoeira
):
    cenario, inicio = create_cenario

    client = authenticated_test_user_client
    data = {
        "inicio": "2026-01-01",
        "nome": "<OTO><NAME>",
    }
    response = client.patch(f"/api/simulador/v1/cenarios/{cenario.pk}/", data=data)
    assert response.status_code == HTTPStatus.OK
    response_json = response.json()
    pk = response_json.pop("id")
    assert pk is not None
    assert response_json["inicio"] == data["inicio"]
    assert response_json["nome"] == data["nome"]
    assert response_json["dias"] == 0
    assert response_json["termino"] == data["inicio"]
    assert response_json["fardoes"] == 0
    assert response_json["rolinhos"] == 0
    assert response_json["total_fardos"] == 0


@pytest.mark.django_db
def test_api_delete_cenario(authenticated_test_user_client, create_cenario):
    cenario, inicio = create_cenario

    client = authenticated_test_user_client

    response = client.delete(f"/api/simulador/v1/cenarios/{cenario.pk}/")
    assert response.status_code == HTTPStatus.NO_CONTENT


@pytest.mark.django_db
def test_api_create_cenario_with_operacao(
    authenticated_test_user_client, create_fazenda, create_algodoeira
):
    fazenda = create_fazenda
    algodoeira = create_algodoeira

    client = authenticated_test_user_client
    data = {
        "inicio": "2026-01-01",
        "nome": "<OTO><NAME>",
        "operacoes": [
            {
                "fazenda": str(fazenda.id),
                "algodoeira": str(algodoeira.id),
                "fardoes": fazenda.fardoes,
                "rolinhos": fazenda.rolinhos,
            },
            {
                "fazenda": str(fazenda.id),
                "algodoeira": str(algodoeira.id),
                "fardoes": fazenda.fardoes,
                "rolinhos": fazenda.rolinhos,
            },
        ],
    }
    response = client.post("/api/simulador/v1/cenarios/", data, format="json")
    assert response.status_code == HTTPStatus.CREATED
    response_json = response.json()
    pk = response_json.pop("id")
    dias = 54
    termino = (
        datetime.strptime(data["inicio"], "%Y-%m-%d").date() + timedelta(days=dias)
    ).strftime("%Y-%m-%d")

    assert pk is not None
    assert response_json["inicio"] == data["inicio"]
    assert response_json["nome"] == data["nome"]
    assert response_json["dias"] == dias
    assert response_json["termino"] == termino
    assert response_json["fardoes"] == 20
    assert response_json["rolinhos"] == 20
    assert response_json["total_fardos"] == 540
