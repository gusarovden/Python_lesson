from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        """Нажать кнопку Checkout."""
        checkout_btn = self.wait.until(EC.element_to_be_clickable(self.checkout_button))
        checkout_btn.click()