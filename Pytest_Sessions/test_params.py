from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass

class TestHubSpot(BaseTest):

    @pytest.mark.parametrize("username,password",[("saikumar@gmail.com"),("admin@123"),("admin@gmail.com"),("admin@123")])

    def test_login(self,username,password):
        """
        this method is used to login our spot application
        :param username:
        :param password:
        :return:
        """
        driver = webdriver.Chrome("C:\\chromedriver.exe")
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_element(By.ID,"username").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
