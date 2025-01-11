import pytest
from django.db.utils import IntegrityError

from src.base.models import Fazenda


@pytest.mark.django_db
def test_create_fazenda(create_fazenda):
    assert create_fazenda.nome == "<NAME>"
    assert create_fazenda.fardoes == 10
    assert create_fazenda.rolinhos == 10


@pytest.mark.django_db(transaction=True)
def test_unique_fazenda(create_fazenda):
    _ = create_fazenda

    with pytest.raises(IntegrityError):
        fazenda = Fazenda(
            nome="<NAME>",
            fardoes=10,
            rolinhos=10,
        )
        fazenda.save()
