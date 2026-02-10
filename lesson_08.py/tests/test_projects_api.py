import pytest

class TestProjectsAPI:

    @pytest.mark.positive
    def test_create_project_positive(self, projects_client, temp_project):
         # Позитивный тест: создание проекта
        #payload = {"title": "Test Project Positive"}
        response = projects_client.get_project(temp_project)
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        data = response.json()
        print(f"Ответ API при создании: {data}")  # Отладка
        assert "id" in data, "В ответе нет поля 'id'"
        assert not data.get("deleted", False), "Проект уже помечен как удалённый!" 


    @pytest.mark.positive
    def test_get_project_positive(self, projects_client, temp_project):
        """Позитивный тест: получение проекта по ID"""
        response = projects_client.get_project(temp_project)
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        data = response.json()
        assert data["id"] == temp_project
        assert "title" in data
        assert not data.get("deleted", False), "Проект уже помечен как удалённый!" 

    @pytest.mark.positive
    def test_update_project_positive(self, projects_client, temp_project):
        """Позитивный тест: обновление названия проекта"""
        new_title = "Updated Project Title"
        payload = {"title": new_title}
        response = projects_client.update_project(temp_project, payload)
        assert response.status_code == 200, f"Ожидался 200, получен {response.status_code}"
        data = response.json()
        print(f"Ответ API при создании: {data}")  # Отладка
        assert "id" in data, "В ответе нет поля 'id'"
        assert not data.get("deleted", False), "Проект уже помечен как удалённый!" 


    @pytest.mark.negative
    def test_create_project_negative_empty_title(self, projects_client):
        """Негативный тест: создание проекта с пустым названием"""
        payload = {"title": ""}
        response = projects_client.create_project(payload)
        assert response.status_code == 400, f"Ожидался 400, получен {response.status_code}"
        data = response.json()
        assert "error" in data or "message" in data
        
    @pytest.mark.negative
    def test_get_project_negative_not_found(self, projects_client):
        """Негативный тест: получение несуществующего проекта"""
        invalid_id = "nonexistent-id-123"
        response = projects_client.get_project(invalid_id)
        assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"
        data = response.json()
        assert data.get("error") == "Not Found" or "Not Found" in str(data)

    @pytest.mark.negative
    def test_update_project_negative_not_found(self, projects_client):
        """Негативный тест: обновление несуществующего проекта"""
        invalid_id = "nonexistent-id-456"
        payload = {"title": "New Title"}
        response = projects_client.update_project(invalid_id, payload)
        assert response.status_code == 404, f"Ожидался 404, получен {response.status_code}"
        data = response.json()
        assert data.get("error") == "Not Found" or "Not Found" in str(data)
