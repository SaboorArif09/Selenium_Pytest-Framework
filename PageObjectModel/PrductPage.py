from email.charset import Charset

from selenium.webdriver.common.by import By

from PageObjectModel.CheckoutPage import CheckOutPage


class ProductPage:
    product = ".card.h-100"
    product_title = ".card-body h4 a"
    desired_product_name = "Blackberry"
    product_button = ".card-footer button"
    cart_button = ".btn.btn-primary"

    def __init__(self, driver):
        self.driver = driver

    def card(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductPage.product)


    def cardTitle(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductPage.product_title)

    def cardButton(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductPage.product_button)

    def checkoutPage(self):
        self.driver.find_element(By.CSS_SELECTOR, ProductPage.cart_button).click()
        checkOutPage =CheckOutPage(self.driver)
        return checkOutPage
