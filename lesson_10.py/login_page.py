from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple

class LoginPage:
    """
    Класс для взаимодействия со страницей авторизации.
    Обеспечивает вход в систему с указанными учётными данными.
    """

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        Args:
            driver: экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.username_input: Tuple[By, str] = (By.ID, "user-name")
        self.password_input: Tuple[By, str] = (By.ID, "password")
        self.login_button: Tuple[By, str] = (By.ID, "login-button")

    def open(self, url: str) -> None:
        """
        Открыть страницу авторизации.

        Args:
            url (str): URL страницы входа
        """
        self.driver.get(url)

    def enter_username(self, username: str) -> None:
        """
        Ввести логин в поле ввода.

        Args:
            username (str): имя пользователя для входа
        """
        username_field = self.wait.until(EC.element_to_be_clickable(self.username_input))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Ввести пароль в поле ввода.

        Args:
            password (str): пароль пользователя
        """
        password_field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self) -> None:
        """
        Нажать кнопку входа для авторизации в системе.
        """
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_btn.click()