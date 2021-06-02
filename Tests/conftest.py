import time

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "IE":
        PATH = "C:\Program Files (x86)\edgedriver_win64\msedgedriver.exe"
        driver = webdriver.Edge(PATH)
    else:
        PATH = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
        driver = webdriver.Chrome(PATH)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
#    driver.implicitly_wait(8)
    request.cls.driver = driver
    yield
    time.sleep(2)
    driver.close()


