from rest_framework import viewsets

from src.base.api.v1.serializers import (
    AlgodoeiraSerializerV1,
    FazendaSerializerV1,
    UserSerializerV1,
)
from src.base.models import Algodoeira, Fazenda, User


class UserViewSetV1(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializerV1


class AlgodoeiraViewSetV1(viewsets.ModelViewSet):
    queryset = Algodoeira.objects.all()
    serializer_class = AlgodoeiraSerializerV1
    search_fields = ("nome",)


class FazendaViewSetV1(viewsets.ModelViewSet):
    queryset = Fazenda.objects.all()
    serializer_class = FazendaSerializerV1
