import pytest
import uuid
import os
from api.projects_api import ProjectsAPI
from decouple import config
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def auth_token():
    token = config("API_AUTH_TOKEN")
    if not token:
        pytest.fail("Переменная API_AUTH_TOKEN не задана в .env или окружении")
    return token

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    url = os.getenv("BASE_URL", "https://yougile.com")
    if not url.startswith("https://"):
        url = f"https://{url}"
    return url.rstrip("/")


@pytest.fixture(scope="module")
def projects_client(auth_token, base_url):
    return ProjectsAPI(base_url, auth_token)


@pytest.fixture()
def temp_project(projects_client):
    # Генерируем уникальное название
    title = f"TEST_AUTO_{uuid.uuid4().hex[:8]}"
    payload = {"title": title}

     # Создание
    response = projects_client.create_project(payload)
    assert response.status_code == 201, f"Создание проекта провалилось: {response.text}"
    project_id = response.json()["id"]
    print(f"[FIXTURE] Создан проект: ID={project_id}")

    yield project_id

    # Очистка через мягкое удаление
    print(f"[FIXTURE] Пытаюсь пометить проект {project_id} как удалённый")
    try:
        delete_response = projects_client.delete_project(project_id)
        if delete_response.status_code in (200, 204):
            data = delete_response.json()
            assert data.get("deleted") is True, "Поле 'deleted' не установлено в true"
            print(f"[FIXTURE] Проект {project_id} успешно помечен как удалённый")
        else:
            print(f"[FIXTURE] Ошибка при удалении: статус {delete_response.status_code}, ответ: {delete_response.text}")
    except Exception as e:
        print(f"[FIXTURE] Исключение при удалении: {e}")
    
def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "positive: Тест на позитивные проверки "
    )
    config.addinivalue_line(
        "markers",
        "negative: Тест на негативные проверки "
    )