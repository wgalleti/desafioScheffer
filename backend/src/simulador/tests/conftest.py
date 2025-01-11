import pytest
from django.utils import timezone

from src.simulador.models import Cenario


@pytest.fixture
def create_cenario(create_test_user):
    inicio = timezone.now().date()

    crenario, _ = Cenario.objects.get_or_create(
        nome="<NAME>",
        inicio=inicio,
        created_by=create_test_user,
    )

    return crenario, inicio
