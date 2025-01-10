from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from unfold.admin import ModelAdmin

from src.base.models import Algodoeira, Fazenda, User

admin.site.unregister(Group)


@admin.register(Fazenda)
class FazendaAdmin(ModelAdmin):
    list_display = (
        "id",
        "nome",
        "fardoes",
        "rolinhos",
    )
    search_fields = ("nome",)


@admin.register(Algodoeira)
class AlgodoeiraAdmin(ModelAdmin):
    list_display = (
        "id",
        "nome",
        "producao",
    )
    search_fields = ("nome",)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ("email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "is_active",
        )


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    search_fields = (
        "username",
        "email",
    )
    list_display = (
        "username",
        "email",
        "name",
        "is_staff",
        "is_superuser",
        "last_login",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal info"),
            {"fields": ("name",)},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "username",
                    "email",
                    "password1",
                    "password2",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "name",
                    "picture",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "groups",
                ),
            },
        ),
        (
            _("Important dates"),
            {
                "fields": (
                    "last_login",
                    "date_joined",
                )
            },
        ),
    )
