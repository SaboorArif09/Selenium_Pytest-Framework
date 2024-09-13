
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
cards = driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
for card in cards:
    pName = card.find_element(By.CSS_SELECTOR, ".card-body h4 a").text.strip()
    if pName == 'Blackberry':
        card.find_element(By.CSS_SELECTOR, ".card-footer button").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys('pa')
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Pakistan")))
driver.find_element(By.LINK_TEXT, "Pakistan").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
assert 'Success' in message

