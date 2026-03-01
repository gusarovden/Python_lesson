
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple

class CalculatorPage:
    """
    Класс для взаимодействия со страницей калькулятора.
    Предоставляет методы для управления элементами калькулятора и получения результатов.
    """

    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора.

        Args:
            driver: экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # Увеличен таймаут для ожидания результата

        # Локаторы
        self.delay_input: Tuple[By, str] = (By.ID, "delay")
        self.button_7: Tuple[By, str] = (By.XPATH, "//span[text()='7']")
        self.button_plus: Tuple[By, str] = (By.XPATH, "//span[text()='+']")
        self.button_8: Tuple[By, str] = (By.XPATH, "//span[text()='8']")
        self.button_equals: Tuple[By, str] = (By.XPATH, "//span[text()='=']")
        self.result_display: Tuple[By, str] = (By.CSS_SELECTOR, ".screen")

    def open(self, url: str) -> None:
        """
        Открыть страницу калькулятора.

        Args:
            url (str): URL страницы калькулятора
        """
        self.driver.get(url)

    def set_delay(self, seconds: int) -> None:
        """
        Установить задержку в поле #delay.

        Args:
            seconds (int): количество секунд задержки
        """
        delay_field = self.wait.until(EC.element_to_be_clickable(self.delay_input))
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button_7(self) -> None:
        """Нажать кнопку '7'."""
        btn = self.wait.until(EC.element_to_be_clickable(self.button_7))
        btn.click()

    def click_button_plus(self) -> None:
        """Нажать кнопку '+'."""
        btn = self.wait.until(EC.element_to_be_clickable(self.button_plus))
        btn.click()

    def click_button_8(self) -> None:
        """Нажать кнопку '8'."""
        btn = self.wait.until(EC.element_to_be_clickable(self.button_8))
        btn.click()

    def click_button_equals(self) -> None:
        """Нажать кнопку '='."""
        btn = self.wait.until(EC.element_to_be_clickable(self.button_equals))
        btn.click()

    def get_result(self) -> str:
        """
        Получить текст из поля результата.

        Returns:
            str: текст из поля результата
        """
        result_elem = self.wait.until(EC.presence_of_element_located(self.result_display))
        self.wait.until(lambda driver: result_elem.text == '15')  # Ждём, пока появится результат
        return result_elem.text