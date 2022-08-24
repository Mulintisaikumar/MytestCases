import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PythonSelFramework.Utility.BaseClass import BaseClass


class TestHomePage(BaseClass):
    class TestHomePage():

     @staticmethod
     def test_formSubmition(self, getData):
        log  = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is"+getData["firstname"])
        homepage.getName().sendkeys(getData["firstname"])
        homepage.getemail1().sendkeys(getData["lastname"])
        homepage.getCheckBox().click()
        sel = Select(homepage.getemail1())
        selectOptonByText(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()

        s = Service("C:\\chromedriver.exe")
        driver = webdriver.Chrome(service = s)
        driver.maximize_window()
        driver.find_element(By.CSS_SELECTOR,"[name= 'name']").send_keys("Sai")
        driver.find_element(By.NAME,"email").send_keys("Kumar")
        driver.find_element(By.ID,"exampleCheck1").click()
        sal = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
        sal.select_by_visible_text("Male")
        driver.find_element(By.XPATH,"//input[@value='submit']").click()

        alertText = driver.find_element(By.CSS_SELECTOR,"[class*='alert-success']").text

        assert ("Success" in alertText)
        self.driver.refresh()


        #@pytest.fixture(params=[{"firstname":"Sai","lastname":"Kumar","gender":"Male"}, ("Sai", "Kumar", "Male"), ("Sai","Pallavi", "Female")])
        #@pytest.fixture(params = HomePage.test_HomePage_data)
        @pytest.fixture(params = HomePage.getTestData("TestCase5"))

        def getData(self, request):
           return request.param



