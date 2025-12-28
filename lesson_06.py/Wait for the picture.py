from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 15)
wait.until(
    EC.presence_of_element_located((By.XPATH, "(//img)[5]"))
)
    
third_img = driver.find_element(By.XPATH, "(//img)[4]")
src_value = third_img.get_attribute("src")
   
print(src_value)
    
driver.quit()
