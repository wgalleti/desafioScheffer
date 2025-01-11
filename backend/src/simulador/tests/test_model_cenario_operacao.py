import pytest
from django.core.exceptions import ValidationError

from src.simulador.models import CenarioOperacao


@pytest.mark.django_db
@pytest.mark.parametrize(
    "fardoes,rolinhos,total_fardos,dias",
    [
        (10, 10, 270, 27),
        (5, 5, 135, 14),
        (5, 5, 135, 14),
        (2, 3, 59, 6),
        (0, 0, 0, 0),
    ],
)
def test_create_cenario_operacao(
    fardoes,
    rolinhos,
    total_fardos,
    dias,
    create_cenario,
    create_algodoeira,
    create_fazenda,
    create_test_user,
):
    cenario, _ = create_cenario
    operacao = CenarioOperacao(
        cenario=cenario,
        algodoeira=create_algodoeira,
        fazenda=create_fazenda,
        fardoes=fardoes,
        rolinhos=rolinhos,
        created_by=create_test_user,
    )

    if fardoes + rolinhos == 0:
        with pytest.raises(ValidationError):
            operacao.save()
    else:
        operacao.save()

        assert operacao.total_fardos == total_fardos
        assert operacao.dias == dias


@pytest.mark.django_db
def test_create_cenario_validation(
    create_cenario,
    create_algodoeira,
    create_fazenda,
    create_test_user,
):
    cenario, _ = create_cenario

    with pytest.raises(ValidationError):
        operacao = CenarioOperacao(
            cenario=cenario,
            algodoeira=create_algodoeira,
            fazenda=create_fazenda,
            fardoes=0,
            rolinhos=0,
            created_by=create_test_user,
        )
        operacao.save()
