import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError

User = get_user_model()


@pytest.mark.django_db
def test_create_user(create_user):
    """
    Test should be can create a new user
    """
    user = create_user(
        username="testuser",
        email="test@example.com",
        password="password123",
    )
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    assert user.check_password("password123")


@pytest.mark.django_db
def test_create_user_without_username(create_user):
    """
    Test should be raise error when username is empty
    """
    with pytest.raises(ValueError):
        create_user(
            username="",
            email="test@example.com",
            password="password123",
        )


@pytest.mark.django_db
def test_unique_email(create_user):
    """
    Test should be raise error when violate email unique constraint
    """
    create_user(
        username="user1",
        email="test@example.com",
        password="password123",
    )
    with pytest.raises(IntegrityError):
        create_user(
            username="user2",
            email="test@example.com",
            password="password123",
        )


@pytest.mark.django_db
def test_invalid_email_format():
    """
    Test should be raise error when email format is invalid
    """
    with pytest.raises(ValidationError):
        user = User(
            username="user",
            email="invalidemail",
            password="password123",
        )
        user.full_clean()


@pytest.mark.django_db
def test_get_full_name(create_user):
    """
    Test should be verified get_full_name function
    """
    user = create_user(
        username="user",
        email="test@example.com",
        password="password123",
        name="John Doe",
    )
    assert user.get_full_name() == "John Doe"
