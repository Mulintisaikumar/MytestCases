import pytest
from selenium import webdriver
import page
from pageObject.LoginPage import LoginPage
from utilities.readproparties import ReadConfig
from utilities.coustomLogger import LogGen


class Test_001_Login():
    '''baseURL = "https://admin-demo.nopcommerce.com/"
    useremail = "admin@yourstore.com"
    password = "admin"'''
    baseURL = ReadConfig.getApplicationURL()
    useremail = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("****** Test_001_Login ******")
        self.logger.info("****** Verfying Home Title ******")
        self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()

        if act_title=="Your store. Login":

            assert True
            self.logger.info("****** Home Page title test is passed ******")
            self.driver.save_screenshot(".\\PytestDemo/pageObject" + "test_homepageTitle.png")
        else:
            self.driver.save_screenshot(".\\PytestDemo/pageObject"+"test_homepageTitle.png")
            self.logger.info("****** Home Page Title Test is faild ******")
            assert False

    def Test_login(self,setup):
        self.logger.info("****** Verfying Login test ******")
        self.driver = setup
        self.driver = webdriver.Chrome("C:\\chromedriver")
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title=="Dashboard / nopCommere administration":
            assert True
            self.logger.info("******Login test is Passed******")
            self.driver.save_screenshot(".\\PytestDemo/pageObject" + "test_login.png")
        else:
            self.logger.info("****** Login Test is faild ******")
            self.driver.save_screenshot(".\\PytestDemo/pageObject" + "test_login.png")
            assert False