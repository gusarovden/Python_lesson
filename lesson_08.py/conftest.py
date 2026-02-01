import uuid
import pytest
from api.projects_api import ProjectsAPI


@pytest.fixture(scope="session")
def auth_token():
    # !!  ПРОПИСАТЬ ТОКЕН ЗДЕСЬ !!
    return "  "  # замените на реальный токен

@pytest.fixture(scope="class")
def projects_client(auth_token):
    """Инициализирует клиент API для тестов."""
    return ProjectsAPI(auth_token)

@pytest.fixture
def temp_project(projects_client):
    """Создаёт временный проект и удаляет его после теста."""
    title = f"Temp Project {uuid.uuid4().hex[:8]}"
    payload = {"title": title}
    response = projects_client.create_project(payload)
    assert response.status_code == 201
    project_id = response.json()["id"]
    yield project_id
    # Очистка
    projects_client.delete_project(project_id)

def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "positive: Тест на позитивные проверки "
    )
    config.addinivalue_line(
        "markers",
        "negative: Тест на негативные проверки "
    )