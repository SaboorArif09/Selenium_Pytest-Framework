import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
expectedList = ["Brinjal - 1 Kg", "Almonds - 1/4 Kg", "Walnuts - 1/4 Kg"]
actualList = []

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, "input[class='search-keyword']").send_keys("al")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
assert count > 0
for product in products:
    actualList.append(product.find_element(By.XPATH, "h4").text)
    product.find_element(By.XPATH, "div/button").click()
assert actualList == expectedList
driver.find_element(By.CSS_SELECTOR, "a[class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
pPrices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in pPrices:
    sum = sum + int(price.text)
print(sum)
tAmount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)
assert sum == tAmount
driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
dAmount = float(driver.find_element(By.CLASS_NAME, "discountAmt").text)
assert dAmount < tAmount