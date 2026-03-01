import allure
import pytest
from selenium import webdriver
from calculator_page_1 import CalculatorPage

@allure.feature("Калькулятор")
@allure.description("Проверка работы калькулятора с задержкой")
class TestCalculator:

    @pytest.fixture(autouse=True)
    def setup(self):
        options = webdriver.ChromeOptions()
        # Подавление логов DevTools и GCM
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-sync")
        # Игнорирование ошибок сертификатов
        options.add_argument("--ignore-certificate-errors")
        # Полное подавление логов
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument("--log-level=3")  # Только критические ошибки

        self.driver = webdriver.Chrome(options=options)
        self.calculator = CalculatorPage(self.driver)
        yield
        self.driver.quit()
    
    @allure.title("Тест сложения 7 + 8 с задержкой 1 секунда")
    @allure.description("Проверяем, что калькулятор правильно складывает числа с задержкой")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_addition_with_delay(self):
        with allure.step("Открытие страницы калькулятора"):
            self.calculator.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        with allure.step("Установка задержки 1 секунда в калбкуляторе"):
            self.calculator.set_delay(1) # Это настройка калькулятора, а не пауза теста

        with allure.step("Нажатие кнопки '7'"):
            self.calculator.click_button_7()

        with allure.step("Нажатие кнопки '+'"):
            self.calculator.click_button_plus()

        with allure.step("Нажатие кнопки '8'"):
            self.calculator.click_button_8()

        with allure.step("Нажатие кнопки '='"):
            self.calculator.click_button_equals()

        with allure.step("Ожидание и проверка результата сложения"):
            result = self.calculator.get_result()
            assert result == "15", f"Ожидалось 15, но получено {result}"
            