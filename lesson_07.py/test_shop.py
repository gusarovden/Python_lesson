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
    # 1. Открыть сайт
    login_page = LoginPage(driver)
    login_page.open("https://www.saucedemo.com/")

    # 2. Авторизоваться как standard_user
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # 3. Добавить товары в корзину
    main_page = MainShopPage(driver)
    main_page.add_backpack_to_cart()
    main_page.add_bolt_tshirt_to_cart()
    main_page.add_onesie_to_cart()

    # 4. Перейти в корзину
    main_page.go_to_cart()

    # 5. Нажать Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 6. Заполнить форму
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_first_name("Иван")
    checkout_page.fill_last_name("Иванов")
    checkout_page.fill_postal_code("12345")