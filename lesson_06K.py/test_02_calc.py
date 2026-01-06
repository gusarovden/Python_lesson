import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from calculator_page import CalculatorPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCalculator(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.driver = webdriver.Chrome(options=options)
        self.calculator = CalculatorPage(self.driver)     # Создаём экземпляр класса.

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.calculator_test
    def test_calculator_with_delay(self):
        
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # Задержка 45.
        self.calculator.set_delay(45)
        
        # Нажать кнопки.
        self.calculator.click_button("7")        
        self.calculator.click_button("+")        
        self.calculator.click_button("8")        
        self.calculator.click_button("=")

        wait = WebDriverWait(self.driver, 60)
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        # Проверка результата 15.
        actual_result = self.calculator.get_result()
        self.assertEqual(actual_result, "15", f"Ожидался результат '15', но получено '{actual_result}'")

