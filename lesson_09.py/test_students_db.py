import pytest
from sqlalchemy import create_engine
from models import Student, create_tables, get_session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Строка подключения к PostgreSQL
DATABASE_URL = (
    f"postgresql://"
    f"{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)

# Создаём движок для PostgreSQL
def get_postgres_engine():
    return create_engine(
        DATABASE_URL,
        echo=True,  # Логирование SQL-запросов
        pool_size=5,
        max_overflow=10
    )

@pytest.fixture(scope="function")
def db_session():
    engine = get_postgres_engine()
    create_tables(engine)
    session = get_session(engine)

    yield session

    # Очистка БД после теста
    session.query(Student).delete()
    session.commit()
    session.close()

@pytest.mark.students
def test_add_student(db_session):
    # Тест добавления студента в БД
    student_name = "Иван Иванов"
    student_email = "ivan@example.com"

    new_student = Student(name=student_name, email=student_email)
    db_session.add(new_student)
    db_session.commit()

    added_student = db_session.query(Student).filter_by(email=student_email).first()

    assert added_student is not None
    assert added_student.name == student_name
    assert added_student.email == student_email
    # Очистка
    db_session.delete(added_student)
    db_session.commit()

@pytest.mark.students
def test_update_student(db_session):
    # Тест изменения студента в БД
    original_name = "Пётр Петров"
    original_email = "petr@example.com"
    student = Student(name=original_name, email=original_email)
    db_session.add(student)
    db_session.commit()

    student_id = student.id

    updated_name = "Павел Павлов"
    updated_email = "pavel@example.com"

    db_session.query(Student).filter_by(id=student_id).update({
        'name': updated_name,
        'email': updated_email
    })
    db_session.commit()

    updated_student = db_session.query(Student).filter_by(id=student_id).first()

    assert updated_student is not None
    assert updated_student.name == updated_name
    assert updated_student.email == updated_email

    # Очистка
    db_session.delete(updated_student)
    db_session.commit()

@pytest.mark.students
def test_delete_student(db_session):
    # Тест удаления студента из БД
    name_to_delete = "Сергей Сергеев"
    email_to_delete = "sergey@example.com"
    student = Student(name=name_to_delete, email=email_to_delete)
    db_session.add(student)
    db_session.commit()

    student_id = student.id

    db_session.delete(student)
    db_session.commit()

    deleted_student = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted_student is None