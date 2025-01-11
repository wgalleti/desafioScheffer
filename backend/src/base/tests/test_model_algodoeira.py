import pytest
from django.db.utils import IntegrityError

from src.base.models import Algodoeira


@pytest.mark.django_db
def test_create_algodoeira(create_algodoeira):
    assert create_algodoeira.nome == "<NAME>"
    assert create_algodoeira.producao == 10


@pytest.mark.django_db(transaction=True)
def test_unique_algodoeira(create_algodoeira):
    _ = create_algodoeira

    with pytest.raises(IntegrityError):
        algodoeira = Algodoeira(
            nome="<NAME>",
            producao=10,
        )
        algodoeira.save()
