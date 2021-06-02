from selenium.webdriver.common.by import By

from Page_Objects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    product_name = (By.XPATH, "//a[href*='shop']/div/h4/a")
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutButton2 = (By.CSS_SELECTOR, "button[class*='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getProductName(self):
        return self.driver.find_elements(*CheckoutPage.product_name)

    def getcheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def getcheckoutButton2(self):
        self.driver.find_element(*CheckoutPage.checkoutButton2).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
