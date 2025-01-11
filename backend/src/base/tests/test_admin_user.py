import pytest
from django.contrib.auth import get_user_model

from src.base.admin import UserCreationForm

User = get_user_model()


@pytest.mark.django_db
class TestUserCreationForm:
    def test_form_valid_data(self):
        form_data = {
            "email": "test@example.com",
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = UserCreationForm(data=form_data)
        assert form.is_valid()

        user = form.save()
        assert user.email == form_data["email"]
        assert user.check_password(form_data["password1"])

    def test_form_invalid_password_mismatch(self):
        form_data = {
            "email": "test@example.com",
            "password1": "securepassword123",
            "password2": "differentpassword",
        }
        form = UserCreationForm(data=form_data)
        assert not form.is_valid()
        assert "password2" in form.errors
        assert form.errors["password2"] == ["Passwords don't match"]

    def test_form_missing_email(self):
        form_data = {
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = UserCreationForm(data=form_data)
        assert not form.is_valid()
        assert "email" in form.errors
        assert form.errors["email"] == ["Este campo é obrigatório."]

    def test_form_save_with_commit_false(self):
        form_data = {
            "email": "test@example.com",
            "password1": "securepassword123",
            "password2": "securepassword123",
        }
        form = UserCreationForm(data=form_data)
        assert form.is_valid()

        user = form.save(commit=False)
        assert user.email == form_data["email"]
        assert not user.pk
