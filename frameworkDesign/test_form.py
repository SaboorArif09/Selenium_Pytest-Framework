import pytest
from selenium.webdriver.common.by import By

from PageObjectModel.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utils.baseClass import BaseClass


class TestForm(BaseClass):
    def test_formSubmission(self, multipleDatasets):
        homePage = HomePage(self.driver)
        homePage.getName().send_keys(multipleDatasets["Name"])
        homePage.getEmail().send_keys(multipleDatasets["Email"])
        homePage.getPassword().send_keys(multipleDatasets["Password"])
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getDropdown(), multipleDatasets["Gender"])
        homePage.getRadio().click()

        homePage.getSubmitButton().click()
        message = homePage.getSucsessAlert().text

        print(message)
        assert "Success" in message
        self.driver.refresh()

@pytest.fixture(params= HomePageData.getDatafromExcel("Testcase2"))
def multipleDatasets(request):
    return request.param

