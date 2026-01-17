from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)  # Увеличен таймаут для ожидания результата

        # Локаторы
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self, url):                 
        self.driver.get(url)  # Открыть страницу калькулятора.  

    def set_delay(self, seconds):
        delay_field = self.wait.until(EC.element_to_be_clickable(self.delay_input))  # Установить задержку в поле #delay.
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button_7(self):        
        btn = self.wait.until(EC.element_to_be_clickable(self.button_7))  # Нажать кнопку '7'.
        btn.click()

    def click_button_plus(self):        
        btn = self.wait.until(EC.element_to_be_clickable(self.button_plus))  # Нажать кнопку '+'.
        btn.click()

    def click_button_8(self):        
        btn = self.wait.until(EC.element_to_be_clickable(self.button_8))  # Нажать кнопку '8'.
        btn.click()

    def click_button_equals(self):        
        btn = self.wait.until(EC.element_to_be_clickable(self.button_equals))  # Нажать кнопку '='.
        btn.click()

    def get_result(self):        
        result_elem = self.wait.until(EC.presence_of_element_located(self.result_display))  # Получить текст из поля результата.        
        self.wait.until(lambda driver: result_elem.text != '7+8') #  Ждём, пока появится результат.
        return result_elem.text