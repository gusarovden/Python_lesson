import logging
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError
from config import BASE_URL, TIMEOUT

logger = logging.getLogger(__name__)

class ProjectsAPI:
    def __init__(self, auth_token: str):
        self.base_url = BASE_URL.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }

    def _request(self, method: str, url: str, **kwargs) -> requests.Response:
        # Обобщённый метод для отправки запросов с обработкой ошибок
        try:
            logger.info(f"{method} {url}")
            response = requests.request(
                method, url, headers=self.headers, timeout=TIMEOUT, **kwargs
            )
            logger.info(f"Status: {response.status_code}")
            logger.debug(f"Response: {response.text}")
            return response
        except Timeout:
            logger.error("Запрос превысил таймаут")
            raise
        except ConnectionError:
            logger.error("Ошибка подключения к серверу")
            raise
        except RequestException as e:
            logger.error(f"Ошибка запроса: {e}")
            raise

    def create_project(self, payload: dict) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects"
        return self._request("POST", url, json=payload)

    def update_project(self, project_id: str, payload: dict) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return self._request("PUT", url, json=payload)

    def get_project(self, project_id: str) -> requests.Response:
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return self._request("GET", url)

    def delete_project(self, project_id: str) -> requests.Response:
        #  DELETE
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = self._request("DELETE", url)
        if response.status_code in [200, 204]:
            return response
