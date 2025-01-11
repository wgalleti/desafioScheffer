from datetime import timedelta

import pytest
from django.db.utils import IntegrityError

from src.base.models import Fazenda
from src.simulador.models import Cenario, CenarioOperacao


@pytest.mark.django_db
def test_create_cenario(create_cenario):
    cenario, inicio = create_cenario
    assert cenario.nome == "<NAME>"
    assert cenario.inicio == inicio
    assert cenario.dias == 0
    assert cenario.termino == inicio
    assert cenario.fardoes == 0
    assert cenario.rolinhos == 0


@pytest.mark.django_db
def test_create_cenario_without_required_field(create_test_user):
    with pytest.raises(IntegrityError):
        cenario = Cenario(
            nome="<NAME>",
            created_by=create_test_user,
        )
        cenario.save()


@pytest.mark.django_db
def test_create_cenario_validation_properties(
    create_cenario,
    create_algodoeira,
    create_fazenda,
    create_test_user,
):
    cenario, inicio = create_cenario

    fazenda2 = Fazenda(
        nome="<NAME>2",
        fardoes=20,
        rolinhos=50,
    )
    fazenda2.save()

    operacao = CenarioOperacao(
        cenario=cenario,
        algodoeira=create_algodoeira,
        fazenda=create_fazenda,
        fardoes=10,
        rolinhos=10,
        created_by=create_test_user,
    )
    operacao.save()

    operacao2 = CenarioOperacao(
        cenario=cenario,
        algodoeira=create_algodoeira,
        fazenda=fazenda2,
        fardoes=20,
        rolinhos=50,
        created_by=create_test_user,
    )
    operacao2.save()

    cenario.refresh_from_db()
    assert cenario.dias == 96
    assert cenario.termino == inicio + timedelta(days=96)
    assert cenario.fardoes == 30
    assert cenario.rolinhos == 60
    assert cenario.total_fardos == 960
