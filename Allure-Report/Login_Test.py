import time

#import Report as Report
from selenium import webdriver
import unittest
#https://www.caterpillar.com/en/brands/cat.html
from selenium.webdriver.common.by import By
import HtmlTestRunner
import sys
import LoginPage

sys.path.append("C://Users\Sai Kumar\PycharmProjects\selenium\Allure-Report")
from pageObject.LoginPage import LoginPage

driver = webdriver.Chrome('C:\\chromedriver.exe')
driver.get("https://www.google.com/")

#enter path
Text_link = driver.find_element(By.XPATH, "//input[@jsaction='paste:puy29d;']")
Text_link.send_keys("https://www.caterpillar.com/en/brands/cat.html")
driver.maximize_window()
#Button
Button_search = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')

for Button_search in Button_search:
    print("your entering in site..!")
else:
    print("Your something Mistake....!")
#site_link
site_link = driver.find_element(By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div.NJo7tc.Z26q7c.uUuwM.jGGQ5e > div.yuRUbf > a > h3")
site_link.click()
#company site
CMP_Site = driver.find_element(By.XPATH, "//a[@data-mega-drawer='mega-company']")
CMP_Site.click()
hst = driver.find_element(By.XPATH, '//*[@id="mega-company"]/div/div/div/div/div/div/div[2]/ul/li[4]/a')
hst.click()
hst.execute_script("window.scrollTo(0, Y)")
for hst in hst:
    print("Ya.. Success..!")
else:
    print("Sorry.. Your Mistaken..!")
class Login_Test(unittest.TestCase):
    baseURL = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        lp.setUserName(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / NopCommerce administration", self.driver.title, "webpage title is not matching")
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main(testRunner = HtmlTestRunner.HTMLTestRunner("output='..\\Allure-Report/Reports"))