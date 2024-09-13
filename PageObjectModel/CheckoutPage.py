from selenium.webdriver.common.by import By


class CheckOutPage:
    checkout_button  = "//button[@class='btn btn-success']"
    country_field = "country"
    checkbox = "//div[@class='checkbox checkbox-primary']"
    purchase_button = "//input[@type='submit']"
    success_message = "//div[@class='alert alert-success alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver

    def checkoutButton(self):
        return self.driver.find_element(By.XPATH, CheckOutPage.checkout_button)

    def countryField(self):
        return self.driver.find_element(By.ID, CheckOutPage.country_field)

    def agreeCheckbox(self):
        return self.driver.find_element(By.XPATH, CheckOutPage.checkbox)

    def purchaseButton(self):
        return self.driver.find_element(By.XPATH, CheckOutPage.purchase_button)

    def susscessMessage(self):
        return self.driver.find_element(By.XPATH, CheckOutPage.success_message)
