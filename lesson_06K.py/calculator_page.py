from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def set_delay(self, delay: int):
        # Хадержка в поле (#delay).
        delay_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def click_button(self, text: str):
        # Нажать кнопку по тексту.
        button = self.driver.find_element(By.XPATH, f"//span[text()='{text}']")
        button.click()

    def get_result(self) -> str:
        # Текст из поля результата (.screen).
        result_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        return result_element.text