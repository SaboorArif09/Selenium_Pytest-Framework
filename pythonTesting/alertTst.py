
from selenium import webdriver
from selenium.webdriver.common.by import By

name = "saboor"
driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "confirmbtn").click()
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert name in alert_text
alert.accept()
# alert.dismiss()