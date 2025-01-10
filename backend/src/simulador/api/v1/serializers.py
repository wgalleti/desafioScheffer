from rest_framework import serializers

from src.simulador.models import Cenario, CenarioOperacao


class CenarioSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Cenario
        fields = "__all__"


class CenarioOperacaoSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = CenarioOperacao
        fields = "__all__"
