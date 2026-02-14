import pytest
from sqlalchemy import create_engine, text
from models import Student, get_test_engine, create_tables, get_session
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
# Строка подключения
DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# 2. Создаём движок
engine = create_engine(
    DATABASE_URL,
    echo=True,  # Логирование SQL-запросов
    pool_size=10,
    max_overflow=20
)

# 3. Создаём фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function")
def db_session():
    # Фикстура для создания сессии БД перед каждым тестом.
    engine = get_test_engine()
    create_tables(engine)
    session = get_session(engine)

    yield session

    # Очистка БД после теста
    session.query(Student).delete()
    session.commit()
    session.close()

@pytest.mark.students
def test_add_student(db_session):
    # Тест добавления студента в БД.
    # Данные для нового студента
    student_name = "Иван Иванов"
    student_email = "ivan@example.com"

    # Создаём объект студента
    new_student = Student(name=student_name, email=student_email)

    # Добавляем в БД
    db_session.add(new_student)
    db_session.commit()

    # Проверяем, что студент добавлен
    added_student = db_session.query(Student).filter_by(email=student_email).first()

    assert added_student is not None
    assert added_student.name == student_name
    assert added_student.email == student_email

    # Удаляем созданного студента (очистка)
    db_session.delete(added_student)
    db_session.commit()

@pytest.mark.students
def test_update_student(db_session):
    # Тест изменения студента в БД.
    # Сначала создаём студента
    original_name = "Пётр Петров"
    original_email = "petr@example.com"
    student = Student(name=original_name, email=original_email)
    db_session.add(student)
    db_session.commit()

    # Получаем ID созданного студента
    student_id = student.id

    # Обновляем данные
    updated_name = "Павел Павлов"
    updated_email = "pavel@example.com"

    db_session.query(Student).filter_by(id=student_id).update({
        'name': updated_name,
        'email': updated_email
    })
    db_session.commit()

    # Проверяем, что данные обновлены
    updated_student = db_session.query(Student).filter_by(id=student_id).first()

    assert updated_student is not None
    assert updated_student.name == updated_name
    assert updated_student.email == updated_email

    # Удаляем обновлённого студента (очистка)
    db_session.delete(updated_student)
    db_session.commit()

@pytest.mark.students
def test_delete_student(db_session):
    # Тест удаления студента из БД
    # Создаём студента для удаления
    name_to_delete = "Сергей Сергеев"
    email_to_delete = "sergey@example.com"
    student = Student(name=name_to_delete, email=email_to_delete)
    db_session.add(student)
    db_session.commit()

    # Сохраняем ID перед удалением
    student_id = student.id

    # Удаляем студента
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студента нет в БД
    deleted_student = db_session.query(Student).filter_by(id=student_id).first()

    assert deleted_student is None