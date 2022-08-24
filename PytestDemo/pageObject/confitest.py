from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser...")
    return driver

#this will get the value from CLI /hooks
#The pytest_addoption hook is passed a parser object.
# pytest addoption is as many times if u want..(adding two perametars..)
def pytest_addoption(parser):
    parser.addoption("--browser")

# this will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")