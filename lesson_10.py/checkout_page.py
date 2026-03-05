from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple

class CheckoutPage:
    """
    Класс для взаимодействия со страницей оформления заказа.
    Позволяет заполнять данные покупателя и получать итоговую стоимость.
    """

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.first_name_input: Tuple[By, str] = (By.ID, "first-name")
        self.last_name_input: Tuple[By, str] = (By.ID, "last-name")
        self.postal_code_input: Tuple[By, str] = (By.ID, "postal-code")
        self.continue_button: Tuple[By, str] = (By.ID, "continue")
        self.total_price: Tuple[By, str] = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, name: str) -> None:
        """
        Заполнить поле имени.

        Args:
            name (str): имя покупателя
        """
        field = self.wait.until(EC.element_to_be_clickable(self.first_name_input))
        field.clear()
        field.send_keys(name)

    def fill_last_name(self, last_name: str) -> None:
        """
        Заполнить поле фамилии.

        Args:
            last_name (str): фамилия покупателя
        """
        field = self.wait.until(EC.element_to_be_clickable(self.last_name_input))
        field.clear()
        field.send_keys(last_name)

    def fill_postal_code(self, code: str) -> None:
        """
        Заполнить поле почтового индекса.

        Args:
            code (str): почтовый индекс
        """
        field = self.wait.until(EC.element_to_be_clickable(self.postal_code_input))
        field.clear()
        field.send_keys(code)

    def click_continue(self) -> None:
        """
        Нажать кнопку Continue для перехода к подтверждению заказа.
        """
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        continue_btn.click()

    def get_total_price(self) -> str:
        """
        Получить текст с итоговой стоимостью заказа.

        Returns:
            str: текст с итоговой ценой
        """
        total_elem = self.wait.until(EC.presence_of_element_located(self.total_price))
        return total_elem.text