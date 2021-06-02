from selenium.webdriver.common.by import By

from Page_Objects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    nameField = (By.CSS_SELECTOR, "input[name='name']")
    emailField = (By.NAME, "email")
    exampleCheck = (By.ID, "exampleCheck1")
    submitButton = (By.XPATH, "//input[@value='Submit']")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")
    gender = (By.ID, "exampleFormControlSelect1")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def getNameField(self):
        return self.driver.find_element(*HomePage.nameField)

    def getEmailField(self):
        return self.driver.find_element(*HomePage.emailField)

    def getExampleCheck(self):
        return self.driver.find_element(*HomePage.exampleCheck)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def getAlertSuccessMessage(self):
        return self.driver.find_element(*HomePage.alert)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)