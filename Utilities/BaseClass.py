import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def test_logging(self):
        my_logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler("logfile.log")
        myFormatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(myFormatter)
        my_logger.addHandler(fileHandler)
        my_logger.setLevel(logging.INFO)
        return my_logger