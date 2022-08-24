from selenium import webdriver
import pytest


@pytest.fixture(params=["chrome","firefox"],scope = 'class')
def init_driver(request):
    if request.param == "chrome":
        driver=webdriver.Chrome("C:\\chromedriver.exe")
    if request.param == "chrome":
        driver=webdriver.Chrome("C:\\chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass

class test_google(Basetest):
    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title == "Google"

    def test_google_url(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.current_url == "Google.com"