from rest_framework import serializers

from src.base.mixins import MixinCreatedBySerializer
from src.simulador.models import Cenario, CenarioOperacao


class CenarioOperacaoBaseSerializerV1(MixinCreatedBySerializer):
    class Meta:
        model = CenarioOperacao
        fields = "__all__"


class CenarioOperacaoListSerializerV1(MixinCreatedBySerializer):

    class Meta:
        model = CenarioOperacao
        fields = (
            "fazenda",
            "algodoeira",
            "fardoes",
            "rolinhos",
            "total_fardos",
            "dias",
        )


class CenarioSerializerV1(MixinCreatedBySerializer):
    dias = serializers.IntegerField(
        read_only=True,
    )
    termino = serializers.DateField(
        read_only=True,
    )
    fardoes = serializers.IntegerField(
        read_only=True,
    )
    rolinhos = serializers.IntegerField(
        read_only=True,
    )
    total_fardos = serializers.IntegerField(
        read_only=True,
    )
    operacoes = CenarioOperacaoListSerializerV1(
        many=True,
        write_only=True,
        required=False,
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["operacoes"] = CenarioOperacaoListSerializerV1(
            instance.operacoes.all(), many=True
        ).data
        return representation

    def create(self, validated_data):
        validated_data.pop("operacoes", [])
        operacoes = self.initial_data.get("operacoes", [])
        instance = super().create(validated_data)

        for operacao in operacoes:
            operacao["cenario"] = str(instance.pk)
            serializer = CenarioOperacaoBaseSerializerV1(
                data=operacao,
                context=self.context,
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()

        instance.refresh_from_db()

        return instance

    class Meta:
        model = Cenario
        fields = "__all__"
