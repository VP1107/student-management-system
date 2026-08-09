import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker

import schema


@pytest.fixture()
def db_session():
    """A fresh in-memory SQLite session with the students table created."""
    engine = create_engine("sqlite:///:memory:")
    schema.Student.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()


def test_create_student(db_session):
    student = schema.Student(name="John Doe", age=19, grade="A", email="john@example.com")
    db_session.add(student)
    db_session.commit()
    db_session.refresh(student)

    assert student.id is not None
    assert student.name == "John Doe"
    assert student.grade == "A"


def test_query_student_by_email(db_session):
    student = schema.Student(name="Jane Doe", age=20, grade="B", email="jane@example.com")
    db_session.add(student)
    db_session.commit()

    result = db_session.query(schema.Student).filter(schema.Student.email == "jane@example.com").first()

    assert result is not None
    assert result.name == "Jane Doe"


def test_update_student_grade(db_session):
    student = schema.Student(name="Sam Smith", age=21, grade="C", email="sam@example.com")
    db_session.add(student)
    db_session.commit()

    student.grade = "A+"
    db_session.commit()
    db_session.refresh(student)

    assert student.grade == "A+"


def test_delete_student(db_session):
    student = schema.Student(name="Alex Lee", age=22, grade="B", email="alex@example.com")
    db_session.add(student)
    db_session.commit()
    student_id = student.id

    db_session.delete(student)
    db_session.commit()

    result = db_session.query(schema.Student).filter(schema.Student.id == student_id).first()
    assert result is None


def test_duplicate_email_rejected(db_session):
    db_session.add(schema.Student(name="Amy A", age=23, grade="A", email="amy@example.com"))
    db_session.commit()

    db_session.add(schema.Student(name="Amy B", age=24, grade="A", email="amy@example.com"))
    with pytest.raises(IntegrityError):
        db_session.commit()
