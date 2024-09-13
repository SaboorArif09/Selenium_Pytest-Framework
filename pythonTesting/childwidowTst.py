import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME, "blinkingText").click()
open_window = driver.window_handles
driver.switch_to.window(open_window[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split('at')[1].strip().split(' ')[0]
print(var)
driver.close()
driver.switch_to.window(open_window[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.ID, "signInBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger").text)

