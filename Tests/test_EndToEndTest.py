import time

import pytest
from selenium import webdriver

#@pytest.mark.usefixtures("setup")
from Page_Objects.CheckoutPage import CheckoutPage
from Page_Objects.ConfirmPage import ConfirmPage
from Page_Objects.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homepage = HomePage(self.driver)

        log = self.test_logging()

        #driver = self.drivercd
        #driver.find_element_by_css_selector("a[href*='shop']").click()
        checkoutpage = homepage.shopItems()
        #products = driver.find_elements_by_xpath("//div[@class='card h-100']")
        #products = homepage.shopItems().find_elements_by_xpath("//div[@class='card h-100']")
        log.info("getting all the card titles")
        products = checkoutpage.getCardTitles()
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            #product_name = checkoutpage.getProductName().text
            if product_name == "Blackberry":
                product.find_element_by_xpath("div/button").click()

        #time.sleep(2)
        #driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        checkoutpage.getcheckoutButton().click()

        #driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        confirmpage = checkoutpage.getcheckoutButton2()

        #driver.find_element_by_css_selector("input[id='country']").send_keys("ind")
        confirmpage.getCountryInput().send_keys("ind")

        #time.sleep(10)
        log.info("verifying the presence of country India")
        self.verifyLinkPresence("India")
        #driver.find_element_by_link_text("India").click()
        confirmpage.clickOption().click()

        #driver.find_element_by_css_selector("//div[@class='checkbox checkbox-primary']").click()
        confirmpage.getCheckBox().click()

        #driver.find_element_by_css_selector("input[type='submit']").click()
        confirmpage.getSubmitButton().click()

        #message = driver.find_element_by_css_selector("div[class*='alert-success']").text
        message = confirmpage.getSuccessMessage().text

        log.info("taking a screenshot of the confirmation message")
        confirmpage.driver.get_screenshot_as_file("clip.png")
        assert "Success" in message

