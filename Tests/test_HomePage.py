import pytest

from Page_Objects.HomePage import HomePage
from TestData.HomePageData import HomePageData

from Utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)
        log = self.test_logging()
        log.info("filling in first name as " + getData["firstname"])
        homepage.getNameField().send_keys(getData["firstname"])
        homepage.getEmailField().send_keys(getData["email"])
        homepage.getExampleCheck().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.getSubmitButton().click()
        message = homepage.getAlertSuccessMessage().text
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param