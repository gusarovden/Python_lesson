import pytest
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

@pytest.mark.test_shop
def test_shop_flow(driver):
    # Открыть сайт
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")

    # Авторизоваться как standard_user
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Добавить товары в корзину
    main_page = MainShopPage(driver)
    main_page.add_backpack_to_cart()
    main_page.add_bolt_tshirt_to_cart()
    main_page.add_onesie_to_cart()

    # Перейти в корзину
    main_page.go_to_cart()

    # Нажать Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Заполнить форму
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_first_name("Иван")
    checkout_page.fill_last_name("Иванов")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()

    # Получить итоговую сумму
    total_price_text = checkout_page.get_total_price()

    # Проверить, что итоговая сумма равна $58.29
    expected_total = "$58.29"
    total_price_clean = total_price_text.replace("Total: ", "")
    assert total_price_clean == expected_total, f"Ожидалась сумма {expected_total}, но получено {total_price_text}"