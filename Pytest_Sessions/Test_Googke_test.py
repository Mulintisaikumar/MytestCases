from selenium import webdriver
import pytest


driver = None


def setup_module(module):
    global driver
    driver=webdriver.Chrome("C:\\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("https://www.youtube.com/")

def teardown_module(module):
    driver.quit()

def test_google_title(self):
    assert self.driver.title == 'YouTube'

def test_Youtube_url(self):
    assert self.driver.current_url =="https://www.youtube.com/"