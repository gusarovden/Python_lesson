import unittest
import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from form_page import FormPage  


class TestForm(unittest.TestCase):

    def setUp(self):
         # Настройки Edge для минимизации логов
        options = Options()
        options.add_argument("--disable-logging")
        options.add_argument("--silent")
        options.add_argument("--log-level=3")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        
        # Сервис с логированием в файл 
        self.service = Service(log_path="edge_service.log")

        self.driver = webdriver.Edge(service=self.service, options=options)
        self.form_page = FormPage(self.driver)        # Создаём экземпляр страницы
        self.wait = WebDriverWait(self.driver, 10)  

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.form_test    
    def test_form_validation(self):
        # Данные для заполнения
        form_data = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        self.form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        self.form_page.fill_form(form_data)

        self.form_page.submit()

        # Ожидать появления элементов успеха
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "alert-success")))

        # Проверить подсветку полей
        success_checks = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_id, expected_text in success_checks.items():
            # Проверяем, что элемент существует
            success_element = self.form_page.get_success_element_by_id(field_id)
            self.assertIsNotNone(success_element, f"Элемент успеха для {field_id} не найден")

            # Проверяем текст (что отображено введённое значение)
            actual_text = self.form_page.get_success_text(field_id)
            self.assertEqual(
                expected_text, actual_text,
                f"Текст в {field_id} не совпадает: ожидалось '{expected_text}', получено '{actual_text}'"
            )
            # Проверяем класс (что это именно «успех»)
            success_class = self.form_page.get_success_class(field_id)
            self.assertIn(
                "alert-success", success_class,
                f"Поле {field_id} не отмечено как успешное (класс: '{success_class}')"
            )
            # Проверить, что zip-code отмечен как ошибка (красный)
            zip_error_element = self.form_page.get_zip_code_error_element()
            self.assertIn(
            "alert-danger", zip_error_element.get_attribute("class"),
            "Zip code не отмечен как ошибочный"
        )
