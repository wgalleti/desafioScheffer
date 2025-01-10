from rest_framework.viewsets import ModelViewSet

from src.simulador.api.v1.serializers import (
    CenarioOperacaoSerializerV1,
    CenarioSerializerV1,
)
from src.simulador.models import Cenario, CenarioOperacao


class CenarioViewSetV1(ModelViewSet):
    queryset = Cenario.objects.all()
    serializer_class = CenarioSerializerV1


class CenarioOperacaoViewSetV1(ModelViewSet):
    queryset = CenarioOperacao.objects.all()
    serializer_class = CenarioOperacaoSerializerV1
