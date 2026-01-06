from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Аавторизация.
    def login(self, username: str, password: str):
        """Войти в аккаунт"""
        username_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys(username)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()

    # Методы для работы с товарами.
    def add_product_to_cart(self, product_name: str):
       
        # Формируем XPath: ищем кнопку с id, содержащим название товара.
        xpath = f"//button[contains(@id, 'add-to-cart-{product_name.lower().replace(' ', '-')}')]"
        add_btn = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        add_btn.click()

    # Методы для перехода в корзину и оформления заказа.
    def go_to_cart(self):
        # Перейти в корзину
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()

    def start_checkout(self):
        # Нажать (Checkout) в корзине.
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_btn.click()

    # Заполнение формы.
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
       
        first_name_input = self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_input.send_keys(first_name)

        last_name_input = self.driver.find_element(By.ID, "last-name")
        last_name_input.send_keys(last_name)

        postal_code_input = self.driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys(postal_code)

        continue_btn = self.driver.find_element(By.ID, "continue")
        continue_btn.click()

    # Получение итоговой суммы.
    def get_total_amount(self) -> str:
       
        total_element = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text