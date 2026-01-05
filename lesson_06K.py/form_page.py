from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

     # Локаторы для ПОЛЕЙ ВВОДА (используются в fill_form).
    FIRST_NAME_INPUT = (By.NAME, "first-name")
    LAST_NAME_INPUT = (By.NAME, "last-name")
    ADDRESS_INPUT = (By.NAME, "address")
    EMAIL_INPUT = (By.NAME, "e-mail")
    PHONE_INPUT = (By.NAME, "phone")
    ZIP_CODE_INPUT = (By.NAME, "zip-code")
    CITY_INPUT = (By.NAME, "city")
    COUNTRY_INPUT = (By.NAME, "country")
    JOB_POSITION_INPUT = (By.NAME, "job-position")
    COMPANY_INPUT = (By.NAME, "company")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Локаторы для ЭЛЕМЕНТОВ УСПЕХА (используются после submit).
    FIRST_NAME_SUCCESS = (By.ID, "first-name")
    LAST_NAME_SUCCESS = (By.ID, "last-name")
    ADDRESS_SUCCESS = (By.ID, "address")
    EMAIL_SUCCESS = (By.ID, "e-mail")
    PHONE_SUCCESS = (By.ID, "phone")
    CITY_SUCCESS = (By.ID, "city")
    COUNTRY_SUCCESS = (By.ID, "country")
    JOB_POSITION_SUCCESS = (By.ID, "job-position")
    COMPANY_SUCCESS = (By.ID, "company")

    # Локатор для ОШИБКИ zip-code.
    ZIP_CODE_ERROR = (By.ID, "zip-code")

    def open(self, url):

        self.driver.get(url)

    def fill_form(self, data):
        
        self.wait.until(EC.presence_of_element_located(self.FIRST_NAME_INPUT)).send_keys(data["first-name"])
        self.wait.until(EC.presence_of_element_located(self.LAST_NAME_INPUT)).send_keys(data["last-name"])
        self.wait.until(EC.presence_of_element_located(self.ADDRESS_INPUT)).send_keys(data["address"])
        self.wait.until(EC.presence_of_element_located(self.EMAIL_INPUT)).send_keys(data["e-mail"])
        self.wait.until(EC.presence_of_element_located(self.PHONE_INPUT)).send_keys(data["phone"])
        self.wait.until(EC.presence_of_element_located(self.ZIP_CODE_INPUT)).clear()  # Оставить пустым
        self.wait.until(EC.presence_of_element_located(self.CITY_INPUT)).send_keys(data["city"])
        self.wait.until(EC.presence_of_element_located(self.COUNTRY_INPUT)).send_keys(data["country"])
        self.wait.until(EC.presence_of_element_located(self.JOB_POSITION_INPUT)).send_keys(data["job-position"])
        self.wait.until(EC.presence_of_element_located(self.COMPANY_INPUT)).send_keys(data["company"])

    def submit(self):
        # Кнопка Submit.
        submit_btn = self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON))
        submit_btn.click()

    def get_success_element_by_id(self, field_id):
        # Найти элемент успеха по id.
        locator = (By.ID, field_id)
        return self.wait.until(EC.presence_of_element_located(locator))

    def get_success_text(self, field_id):
        # Получить текст элемента успеха.
        element = self.get_success_element_by_id(field_id)
        return element.text

    def get_success_class(self, field_id):
        # Получить класс элемента успеха.
        element = self.get_success_element_by_id(field_id)
        return element.get_attribute("class")

    def get_zip_code_error_element(self):
        # Получить элемент ошибки для zip-code.
        return self.wait.until(EC.presence_of_element_located(self.ZIP_CODE_ERROR))