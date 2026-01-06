import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from shop_page import ShopPage

class TestShopPurchase(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--log-level=3")
        self.driver = webdriver.Firefox(options=options)
        self.shop = ShopPage(self.driver)  # Создаём экземпляр класса

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.shop_test
    def test_purchase_flow(self):
        # 1. Открыть сайт
        self.driver.get("https://www.saucedemo.com/")

        # 2. Авторизоваться
        self.shop.login("standard_user", "secret_sauce")

        # 3. Добавить товары в корзину
        self.shop.add_product_to_cart("Sauce Labs Backpack")
        self.shop.add_product_to_cart("Sauce Labs Bolt T-Shirt")
        self.shop.add_product_to_cart("Sauce Labs Onesie")
        
        # 4. Перейти в корзину и начать оформление заказа
        self.shop.go_to_cart()
        self.shop.start_checkout()
        
        # 5. Заполнить форму
        self.shop.fill_checkout_form("Иван", "Петров", "123456")
       
        # 6. Получить и проверить итоговую сумму
        actual_total = self.shop.get_total_amount()
        expected_total = "$58.29"
        self.assertIn(expected_total, actual_total,
                        f"Ожидалась сумма '{expected_total}', но получено '{actual_total}'")

