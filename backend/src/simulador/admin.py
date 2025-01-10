from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from src.simulador.models import Cenario, CenarioOperacao


class CenarioOperacaoInLineAdmin(StackedInline):
    model = CenarioOperacao
    tab = True
    extra = 0


@admin.register(Cenario)
class CenarioAdmin(ModelAdmin):
    inlines = [CenarioOperacaoInLineAdmin]
    list_display = (
        "nome",
        "inicio",
        "termino",
        "dias",
        "fardoes",
        "rolinhos",
    )
