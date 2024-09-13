from selenium.webdriver.common.by import By

from PageObjectModel.HomePage import HomePage
from utils.baseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        productPage = homePage.clickOnShop()
        log.info("getting all the cart titles")
        cards = self.driver.find_elements(By.CSS_SELECTOR, ".card.h-100")
        for card in cards:
            pName = card.find_element(By.CSS_SELECTOR, ".card-body h4 a").text.strip()
            log.info(pName)
            if pName == 'Blackberry':
                card.find_element(By.CSS_SELECTOR, ".card-footer button").click()
        checkOutPage = productPage.checkoutPage()
        checkOutPage.checkoutButton().click()
        log.info("entring country name as pakistan")
        checkOutPage.countryField().send_keys('pa')
        self.Explicitly_wait("Pakistan")
        self.driver.find_element(By.LINK_TEXT, "Pakistan").click()
        checkOutPage.agreeCheckbox().click()
        checkOutPage.purchaseButton().click()
        message = checkOutPage.susscessMessage().text
        log.info("Message recieved from application is "+message)
        assert 'Success' in message

