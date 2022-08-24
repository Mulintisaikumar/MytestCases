from allure_commons.types import AttachmentType
from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:

    @allure.severity(allure.severity_level.MINOR)
    def test_Logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element((By.XPATH, '//*[@id="divLogo"]/img'))
        status.is_displayed()
        self.driver.close()

        if status == True:
            assert True
        else:
            assert False

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys('admin1230')
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        act_title = self.driver.title
        self.driver.close()

        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login_screen",
                          attachment_type = AttachmentType.PNG)
            assert False
#        self.driver.close()