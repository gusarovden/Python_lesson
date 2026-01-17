from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self, url):
        """Открыть страницу авторизации."""
        self.driver.get(url)

    def enter_username(self, username):
        """Ввести логин."""
        username_field = self.wait.until(EC.element_to_be_clickable(self.username_input))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Ввести пароль."""
        password_field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        """Нажать кнопку входа."""
        login_btn = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_btn.click()