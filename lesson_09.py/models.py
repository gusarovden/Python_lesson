from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

def get_test_engine():
    # Создаёт тестовый движок БД (SQLite)
    return create_engine('sqlite:///test_students.db', echo=False)

def create_tables(engine):
    # Создаёт таблицы в БД
    Base.metadata.create_all(engine)

def get_session(engine):
    # Возвращает сессию для работы с БД
    Session = sessionmaker(bind=engine)
    return Session()