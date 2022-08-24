from selenium import webdriver
import pytest

@pytest.fixture(params=["chrome"],scope = 'class')
def init_driver(request):
    if request.param == "chrome":
        driver=webdriver.Chrome("C:\\chromedriver.exe")
    if request.param == "chrome":
        driver=webdriver.Chrome("C:\\chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.close()