from selenium.webdriver.common.by import By

from PageObjectModel.PrductPage import ProductPage

class HomePage:
    shop = "//a[contains(@href,'shop')]"
    name = "input[name='name']"
    email = "email"
    password = "exampleInputPassword1"
    checkbox = "exampleCheck1"
    dropdown = "exampleFormControlSelect1"
    radio = "#inlineRadio1"
    button = "//input[@type='submit']"
    alert = "alert-success"

    def __init__(self, driver):
        self.driver = driver

    def clickOnShop(self):
      self.driver.find_element(By.XPATH, HomePage.shop).click()
      productPage = ProductPage(self.driver)
      return productPage

    def getName(self):
        return self.driver.find_element(By.CSS_SELECTOR, HomePage.name)

    def getEmail(self):
        return self.driver.find_element(By.NAME, HomePage.email)

    def getPassword(self):
        return self.driver.find_element(By.ID, HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(By.ID, HomePage.checkbox)

    def getDropdown(self):
        return self.driver.find_element(By.ID, HomePage.dropdown)

    def getRadio(self):
        return self.driver.find_element(By.CSS_SELECTOR, HomePage.radio)

    def getSubmitButton(self):
        return self.driver.find_element(By.XPATH, HomePage.button)

    def getSucsessAlert(self):
        return self.driver.find_element(By.CLASS_NAME, HomePage.alert)