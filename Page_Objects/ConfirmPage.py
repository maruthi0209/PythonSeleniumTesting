from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryInput = (By.CSS_SELECTOR, "input[id='country']")
    option = (By.LINK_TEXT, "India")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    submitButton = (By.CSS_SELECTOR, "input[class*='btn-success']")
    successmessage = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def getCountryInput(self):
        return self.driver.find_element(*ConfirmPage.countryInput)

    def clickOption(self):
        return self.driver.find_element(*ConfirmPage.option)

    def getCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getSubmitButton(self):
        return self.driver.find_element(*ConfirmPage.submitButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successmessage)