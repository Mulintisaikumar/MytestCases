from selenium import webdriver
import pytest


driver = None

@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("______setup_______")
    driver=webdriver.Chrome("C:\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.youtube.com/")

    yield
    print("__________teardown_______")
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_google_title(init_driver):
    assert driver.title == 'YouTube'

@pytest.mark.usefixtures("init_driver")
def test_Youtube_url(init_driver):
    assert driver.current_url =="https://www.youtube.com/"