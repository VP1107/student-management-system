import pytest
from pydantic import ValidationError

import model


def test_student_create_accepts_valid_data():
    student = model.StudentCreate(name="Test User", age=19, grade="A", email="test@example.com")

    assert student.name == "Test User"
    assert student.age == 19
    assert student.email == "test@example.com"


def test_student_create_rejects_invalid_age():
    with pytest.raises(ValidationError):
        model.StudentCreate(name="Test User", age=200, grade="A", email="test@example.com")


def test_student_create_rejects_non_positive_age():
    with pytest.raises(ValidationError):
        model.StudentCreate(name="Test User", age=0, grade="A", email="test@example.com")


def test_student_create_rejects_invalid_email():
    with pytest.raises(ValidationError):
        model.StudentCreate(name="Test User", age=19, grade="A", email="not-an-email")
