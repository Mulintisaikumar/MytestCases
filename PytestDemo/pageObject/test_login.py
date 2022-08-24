import pytest
from selenium import webdriver
import page
from pageObject.LoginPage import LoginPage

class Test_001_Login:
    '''baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"'''
    baseURL = "https://demo.guru99.com/insurance/v1/index.php"
    username = "saikumar636369@gmail.com"
    password = "Sai@1435"
    def test_homePageTitle(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        #if act_title=="Your store. Login":
        if act_title=="Broker Insurance WebPage":
            assert True
            #self.driver.save_screenshot(".\\PytestDemo/pageObject" + "test_homepageTitle.png")
        else:
            #self.driver.save_screenshot(".\\PytestDemo/pageObject"+"test_homepageTitle.png")
            assert False

    def Test_login(self,setup):
        self.driver = webdriver.Chrome("C:\\chromedriver")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        #if act_title=="Dashboard / nopCommere administration":
        if act_title=="Demo Site":
            assert True
            self.driver.save_screenshot(".\\PytestDemo/pageObject" + "test_login.png")
        else:
            self.driver.save_screenshot(".\\PytestDemo/pageObject" + "test_login.png")
            assert False