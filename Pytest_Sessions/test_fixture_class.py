from selenium import webdriver
import pytest

@pytest.fixture(scope='class')
def init_driver(request):
    driver=webdriver.Chrome("C:\\chromedriver.exe")
    request.cls.driver = driver
    yield
    driver.close()

@pytest.fixture(scope='class')
def init_ch_driver(request):
    drievr1 = webdriver.Chrome("C:\\chromedriver.exe")
    request.cls.driver=drievr1
    yield
    drievr1.close()

@pytest.mark.usefixtures("init_ch_driver")
class Base_Chrome_Test:
    pass
class Test_Google_title_chrome(Base_Chrome_Test):

    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title=="Google"
