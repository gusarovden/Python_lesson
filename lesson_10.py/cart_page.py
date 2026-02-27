from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple

class CartPage:
    """
    Класс для взаимодействия со страницей корзины.
    Предоставляет методы для работы с элементами корзины и перехода к оформлению заказа.
    """

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        Args:
            driver: экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.checkout_button: Tuple[By, str] = (By.ID, "checkout")

    def click_checkout(self) -> None:
        """
        Нажать кнопку Checkout для перехода к оформлению заказа.
        """
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout_btn.click()