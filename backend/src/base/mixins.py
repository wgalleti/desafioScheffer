import uuid

from django.db import models


class MixinModelUUID(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    def __str__(self):
        if hasattr(self, "name"):
            return self.name
        return f"{self.id}"

    class Meta:
        abstract = True


class MixinModelCreatedData(models.Model):
    created_by = models.ForeignKey(
        to="base.User",
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_users",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        if hasattr(self, "name"):
            return self.name

        if hasattr(self, "description"):
            return self.description

        return f"{self.pk}"

    class Meta:
        abstract = True
