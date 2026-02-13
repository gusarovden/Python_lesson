import requests
from requests.exceptions import RequestException, Timeout
import logging

logger = logging.getLogger(__name__)

class ProjectsAPI:
    def __init__(self, base_url: str, auth_token: str):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            logger.info(f"{method} {url}")
            response = requests.request(
                method, url, headers=self.headers, timeout=10, **kwargs
            )
            logger.info(f"Status: {response.status_code}")
            return response
        except Timeout:
            logger.error("Запрос превысил таймаут (10 сек)")
            raise
        except RequestException as e:
            logger.error(f"Ошибка запроса: {e}")
            raise

    def create_project(self, payload: dict) -> requests.Response:
        return self._request("POST", "/api-v2/projects", json=payload)

    def update_project(self, project_id: str, payload: dict) -> requests.Response:
        return self._request("PUT", f"/api-v2/projects/{project_id}", json=payload)

    def get_project(self, project_id: str) -> requests.Response:
        return self._request("GET", f"/api-v2/projects/{project_id}")
    
    def delete_project(self, project_id: str) -> requests.Response:
        payload = {"deleted": True}
        return self._request("PUT", f"/api-v2/projects/{project_id}", json=payload)