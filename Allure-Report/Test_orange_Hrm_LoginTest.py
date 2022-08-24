from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\chromedriver.exe')
#path
path = driver.get("https://opensource-demo.orangehrmlive.com/")
def Login(self, driver=driver):
    self.driver = driver.get('https://opensource-demo.orangehrmlive.com/')
    driver = driver.find_element(By.ID, "txtUsername")
    driver.send_keys('Admin')
    self.driver = driver.find_element(By.ID, "txtPassword").send_keys('admin123')
    act_title = self.driver.title
    print("success..!")


    if act_title == "OrangeHRM123":
        print(act_title)