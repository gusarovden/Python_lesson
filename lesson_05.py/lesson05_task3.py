from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "input")))

input_field.send_keys("Sky")

import time

time.sleep(3)

input_field.clear()

input_field.send_keys("Pro")

import time

time.sleep(3)

driver.quit()
