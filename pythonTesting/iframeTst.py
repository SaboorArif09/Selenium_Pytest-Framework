import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.find_element(By.CLASS_NAME, "tox-button").click()
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to handle frames")
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h3").text)

