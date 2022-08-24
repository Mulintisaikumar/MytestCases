import pytest
from selenium import webdriver


def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome("C:\\chromedriver")

    if request.param=="chrome":
        web_driver = webdriver.Chrome("C:\\chromedriver")

    request.cls.driver = web_driver
    #web_driver.implicitly_wait(5)
    yield
    web_driver.close()
