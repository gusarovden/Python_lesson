from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_price = (By.CLASS_NAME, "summary_total_label")

    def fill_first_name(self, name):
        """Заполнить имя."""
        field = self.wait.until(EC.element_to_be_clickable(self.first_name_input))
        field.clear()
        field.send_keys(name)

    def fill_last_name(self, last_name):
        """Заполнить фамилию."""
        field = self.wait.until(EC.element_to_be_clickable(self.last_name_input))
        field.clear()
        field.send_keys(last_name)

    def fill_postal_code(self, code):
        """Заполнить почтовый индекс."""
        field = self.wait.until(EC.element_to_be_clickable(self.postal_code_input))
        field.clear()
        field.send_keys(code)

    def click_continue(self):
        """Нажать Continue."""
        continue_btn = self.wait.until(EC.element_to_be_clickable(self.continue_button))
        continue_btn.click()

    def get_total_price(self):
        """Получить итоговую стоимость."""
        total_elem = self.wait.until(EC.presence_of_element_located(self.total_price))
        return total_elem.text
