from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.base.mixins import MixinModelUUID


class Fazenda(MixinModelUUID):
    nome = models.CharField(
        max_length=255,
        unique=True,
    )
    fardoes = models.PositiveIntegerField(
        default=0,
    )
    rolinhos = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _("Fazenda")
        verbose_name_plural = _("Fazendas")


class Algodoeira(MixinModelUUID):
    nome = models.CharField(
        max_length=255,
        unique=True,
    )
    producao = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = _("Algodoeira")
        verbose_name_plural = _("Algodoeiras")


class User(AbstractUser):
    name = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Name"),
    )
    first_name = None
    last_name = None
    email = models.EmailField(
        unique=True,
        verbose_name=_("Email"),
    )
    username = models.CharField(
        blank=True,
        max_length=255,
        unique=True,
        verbose_name=_("Username"),
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return self.name
