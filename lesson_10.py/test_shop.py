import pytest
import allure
from selenium import webdriver
from login_page import LoginPage
from main_shop_page import MainShopPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Покупка товаров")
@allure.description("Полный сценарий покупки: авторизация, добавление товаров в корзину, оформление заказа")
def test_shop_flow(driver):
    """
    Тест полного сценария покупки:
    1. Авторизация
    2. Добавление товаров в корзину
    3. Оформление заказа
    4. Проверка итоговой суммы
    """

    with allure.step("Открытие сайта и авторизация"):
        login_page = LoginPage(driver)
        login_page.open("https://www.saucedemo.com/")

        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

    with allure.step("Добавление товаров в корзину"):
        main_page = MainShopPage(driver)
        main_page.add_backpack_to_cart()
        main_page.add_bolt_tshirt_to_cart()
        main_page.add_onesie_to_cart()

    with allure.step("Переход в корзину и нажатие Checkout"):
        main_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнение формы оформления заказа"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_first_name("Иван")
        checkout_page.fill_last_name("Иванов")
        checkout_page.fill_postal_code("12345")
        checkout_page.click_continue()

    with allure.step("Проверка итоговой суммы заказа"):
        total_price_text = checkout_page.get_total_price()

        # Очистка текста от лишних символов
        total_price_clean = total_price_text.replace("Total: ", "").strip()

        expected_total = "$58.29"

        with allure.step(f"Проверка: ожидаемая сумма {expected_total}, фактическая {total_price_clean}"):
            assert total_price_clean == expected_total, \
                f"Ожидалась сумма {expected_total}, но получено {total_price_text}"

        allure.attach(
            f"Ожидаемая сумма: {expected_total}\nФактическая сумма: {total_price_clean}",
            name="Результаты проверки суммы",
            attachment_type=allure.attachment_type.TEXT
        )