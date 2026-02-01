import uuid
import requests
import pytest
import json
from json import JSONDecodeError

def assert_json_response(response: requests.Response) -> dict:
    # Проверяет, что ответ — JSON, и возвращает его.
    content_type = response.headers.get("Content-Type", "")
    if "application/json" not in content_type:
        pytest.fail(f"Ответ не JSON: Content-Type={content_type}")
    try:
        return response.json()
    except JSONDecodeError as e:
        pytest.fail(f"Не удалось декодировать JSON: {e}")

@pytest.mark.usefixtures("projects_client")
class TestProjectsAPI:

    @pytest.mark.positive
    def test_create_project_success(self, projects_client):
        payload = {"title": f"Test Project {uuid.uuid4().hex[:8]}"}
        response = projects_client.create_project(payload)

        assert response.status_code == 201, (
            f"Создание провалилось: {response.status_code}, {response.text}"
        )

        data = assert_json_response(response)
        assert "id" in data, "В ответе нет 'id'"
        assert data["id"], "ID пуст"
        print(f"[INFO] Проект создан. ID: {data['id']}")


    @pytest.mark.positive
    def test_get_project_success(self, projects_client, temp_project):
        response = projects_client.get_project(temp_project)
        assert response.status_code == 200, (
            f"Получение провалилось: {response.status_code}"
        )

        data = assert_json_response(response)
        assert data["id"] == temp_project, "ID не совпадает"
        assert "title" in data, "Нет 'title' в ответе"

    @pytest.mark.positive
    def test_update_project_success(self, projects_client, temp_project):
        new_title = "Updated Title"
        payload = {"title": new_title}
        response = projects_client.update_project(temp_project, payload)

        assert response.status_code == 200, (
            f"Обновление провалилось: {response.status_code}"
        )

        # Проверяем, что изменения применились
        get_response = projects_client.get_project(temp_project)
        data = assert_json_response(get_response)
        assert data["title"] == new_title, f"Название не обновилось до '{new_title}'"

    @pytest.mark.negative
    def test_create_project_no_title(self, projects_client):
        payload = {"description": "Без названия"}
        response = projects_client.create_project(payload)

        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )

        data = assert_json_response(response)
        messages = data.get("message", [])
        assert any("title" in msg.lower() for msg in messages), (
            f"Нет упоминания 'title' в ошибках: {messages}"
        )

    @pytest.mark.negative
    def test_create_project_invalid_title_type(self, projects_client):
        payload = {"title": 12345}
        response = projects_client.create_project(payload)

        assert response.status_code == 400, (
            f"Ожидался 400, получен {response.status_code}"
        )

        data = assert_json_response(response)
        messages = data.get("message", [])
        assert any("must be a string" in msg.lower() for msg in messages), (
            f"Нет сообщения о типе title: {messages}"
        )

    @pytest.mark.negative
    def test_get_project_not_found(self, projects_client):
        non_existent_id = "invalid-uuid-format"
        response = projects_client.get_project(non_existent_id)

        assert response.status_code == 404, (
            f"Ожидался 404, получен {response.status_code}"
        )

    @pytest.mark.negative
    def test_update_project_not_found(self, projects_client):
        non_existent_id = "invalid-uuid-format"
        payload = {"title": "New Title"}
        response = projects_client.update_project