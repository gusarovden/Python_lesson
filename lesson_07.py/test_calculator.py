import pytest
from selenium import webdriver
from calculator_page_1 import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.test_calculator
def test_calculator_with_delay(driver):
    
    # Создаём экземпляр страницы.
    calc_page = CalculatorPage(driver)

    # Открываем страницу калькулятора.
    calc_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Устанавливаем задержку 45 секунд.
    calc_page.set_delay(45)

    # Нажимаем кнопки: 7 + 8 =.
    calc_page.click_button_7()
    calc_page.click_button_plus()
    calc_page.click_button_8()
    calc_page.click_button_equals()

    # Получаем результат.
    result = calc_page.get_result()

    # Проверяем, что результат равен '15'.
    assert result == "15", f"Ожидался результат '15', но получено '{result}'"
    