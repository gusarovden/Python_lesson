from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import Tuple

class MainShopPage:
    """
    Класс для взаимодействия с главной страницей магазина.
    Позволяет добавлять товары в корзину и переходить к ней.
    """

    def __init__(self, driver):
        """
        Инициализация главной страницы магазина.

        Args:
            driver: экземпляр WebDriver для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.backpack_add_button: Tuple[By, str] = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
        self.bolt_tshirt_add_button: Tuple[By, str] = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.onesie_add_button: Tuple[By, str] = (By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']")
        self.cart_link: Tuple[By, str] = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self) -> None:
        """
        Добавить рюкзак в корзину.
        """
        btn = self.wait.until(EC.element_to_be_clickable(self.backpack_add_button))
        btn.click()

    def add_bolt_tshirt_to_cart(self) -> None:
        """
        Добавить футболку в корзину.
        """
        btn = self.wait.until(EC.element_to_be_clickable(self.bolt_tshirt_add_button))
        btn.click()

    def add_onesie_to_cart(self) -> None:
        """
        Добавить комбинезон в корзину.
        """
        btn = self.wait.until(EC.element_to_be_clickable(self.onesie_add_button))
        btn.click()

    def go_to_cart(self) -> None:
        """Перейти в корзину."""
        cart_link = self.wait.until(EC.element_to_be_clickable(self.cart_link))
        cart_link.click()
        