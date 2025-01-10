from datetime import timedelta

from django.db import models

from src.base.mixins import MixinModelCreatedData, MixinModelUUID


class Cenario(MixinModelUUID, MixinModelCreatedData):
    nome = models.CharField(
        "nome",
        max_length=255,
    )
    inicio = models.DateField()

    @property
    def dias(self):
        return sum(self.operacoes.all().values_list("dias", flat=True))

    @property
    def termino(self):
        if self.dias <= 0:
            return self.inicio

        return self.inicio + timedelta(days=self.dias)

    @property
    def fardoes(self):
        return sum(self.operacoes.all().values_list("fardoes", flat=True))

    @property
    def rolinhos(self):
        return sum(self.operacoes.all().values_list("rolinhos", flat=True))

    class Meta:
        verbose_name = "cenario"
        verbose_name_plural = "cenarios"

    def __str__(self):
        return self.nome


class CenarioOperacao(MixinModelUUID, MixinModelCreatedData):
    class Producao(models.IntegerChoices):
        FARDAO = 22, "FARDAO"
        ROLINHO = 5, "ROLINHO"

    cenario = models.ForeignKey(
        to="simulador.Cenario",
        on_delete=models.CASCADE,
        related_name="operacoes",
    )
    fazenda = models.ForeignKey(
        to="base.Fazenda",
        on_delete=models.CASCADE,
        related_name="operacoes",
    )
    algodoeira = models.ForeignKey(
        to="base.Algodoeira",
        on_delete=models.CASCADE,
        related_name="operacoes",
    )
    fardoes = models.PositiveIntegerField(
        default=0,
    )
    rolinhos = models.PositiveIntegerField(
        default=0,
    )
    total_fardos = models.PositiveIntegerField(
        default=0,
    )
    dias = models.PositiveIntegerField(
        default=0,
    )

    def save(
        self,
        *args,
        **kwargs,
    ):
        self.total_fardos = (
            self.fardoes * CenarioOperacao.Producao.FARDAO
            + self.rolinhos * CenarioOperacao.Producao.ROLINHO
        )
        self.dias = self.total_fardos / self.algodoeira.producao
        super().save(*args, **kwargs)
